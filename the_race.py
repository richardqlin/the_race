import pygame
import time
import random
from pygame.locals import *
pygame.init()
width =800
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Spac Vadré')
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)


finishers=0
lap=2
class Ball:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.lap_count=0

        self.radius = 10
        self.speed = random.randint(1,4)
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
   
    def move(self):
        if self.x >= width-10:
            self.speed= - random.randint(1,4) 
        elif self.x<=10:
            self.speed = random.randint(1,4) 
            self.lap_count += 1

            
           
ball_list = []
##ball_list = [Ball(25,i*50+50,(255,255,255))  for i in range(10) ]
game = True
while game:
    pygame.time.delay(1)
    pygame.display.update()
    screen.fill(black)
    for b in ball_list:
        b.draw()
        b.move()
        if b.lap_count<lap:
            b.x += b.speed
        if b.lap_count == lap:
            finishers +=1
        print(finishers)
        if finishers == 1 and b.lap_count==lap :
            print('red')
            b.x=10
            b.color=(255,0,0)  
        elif finishers ==2 and b.lap_count==lap :
            b.color=(0,255,0)    
            b.x=10  
            print('green')
        elif finishers ==3 and b.lap_count==lap:
            b.color=(0,0,255)
            print('blue')
            b.x=10
            finishers +=1
    if finishers >= 11:
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                ball_list = [Ball(25,i*50+50,(255,255,255))  for i in range(10) ]


print('game over')
