import pygame
from datetime import datetime   #시간 관련 함수
from datetime import timedelta
import random

pygame.init()
#전역변수
WHITE = (255,255,255)
size = [400,300]
screen = pygame.display.set_mode(size)
RED = (255,0,0)
GREEN = (0,255,0)

done = False
clock = pygame.time.Clock()
last_moved_time = datetime.now()

#키입력 사전형
KEY_DIRECTION = {
    pygame.K_UP: 'N',
    pygame.K_DOWN: 'S',
    pygame.K_LEFT: 'W',
    pygame.K_RIGHT: 'E',
}


def draw_block(screen, color, position):
    block = pygame.Rect((position[0]*20,position[1]*20),(20,20))
    pygame.draw.rect(screen,color,block)

#클래스
class Snake:
    def __init__(self):
        self.positions = [(2,0),(1,0),(0,0)] #뱀의 위치, 2,0이 머리이다
        self.direction = ''

    def draw(self):
        for position in self.positions:
            draw_block(screen,GREEN,position)

    def move(self):
        head_position = self.positions[0]
        x, y = head_position
        if self.direction == 'N':
            self.positions = [(x,y-1)] + self.positions[:-1]
            print(self.positions)
        elif self.direction == 'S':
            self.positions = [(x,y+1)] + self.positions[:-1]
            print(self.positions)
        elif self.direction == 'W':
            self.positions = [(x-1,y)] + self.positions[:-1]
            print(self.positions)
        elif self.direction == 'E':
            self.positions = [(x+1,y)] + self.positions[:-1]
            print(self.positions)

    #사과먹었을떄 뱀 성장
    def grow(self):
        tail_position = self.positions[-1] #마지막의 리스트 요소
        x, y = tail_position
        if self.direction =='N':
            # .append()를 사용하면 값이 뒤에 추가된다
            # ex) [(2, 0), (1, 0), (0, 0)] 라면, positions.append((10, 20))의 결과는 [(2, 0), (1, 0), (0, 0), (10, 20)]이 된다
            self.positions.append((x,y - 1))
        elif self.direction == 'S':
            self.positions.append((x, y + 1))
        elif self.direction == 'W':
            self.positions.append((x - 1, y))
        elif self.direction == 'E':
            self.positions.append((x + 1, y))

class Apple:
    def __init__(self, position = (5,5)):
        self.position = position

    def draw(self):
        draw_block(screen,RED,self.position)



#루프
def runGame():
    global done, last_moved_time, moving_direction
    #게임 시작시 뱀과 사과를 초기화
    snake = Snake()
    apple = Apple()

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]
            
        if timedelta(seconds=0.5) <= datetime.now() - last_moved_time:
            snake.move()
        if snake.positions[0] == apple.position:
            snake.grow()
            apple.position = (random.randint(0,19),random.randint(0,15))
            print("apple!:",apple.position)
        #꼬리에 닿았을때 종료
        if snake.positions[0] in snake.positions[1:]:
            done = True

        snake.draw()
        apple.draw()
        pygame.display.update()

runGame()
pygame.quit()