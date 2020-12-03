import pygame
import random
import time
from enum import Enum
import sys

pygame.init()
size_x = 800
size_y = 600
window = pygame.display.set_mode((size_x, size_y))

pygame.mixer.music.load('nurzh.mp3')
pygame.mixer.music.play()

bulletSound=pygame.mixer.Sound('bullet.wav')
game_overSound=pygame.mixer.Sound('game_over.wav')

Directions = {
    pygame.K_RIGHT: 'RIGHT', 
    pygame.K_LEFT: 'LEFT',
    pygame.K_UP: 'UP', 
    pygame.K_DOWN: 'DOWN',
    pygame.K_d: 'RIGHT', 
    pygame.K_a: 'LEFT',
    pygame.K_w: 'UP', 
    pygame.K_s: 'DOWN'
}

class Tank:
    def __init__(self, x, y, speed, color, shoot):
        self.x = x
        self.y = y
        self.score = 3
        self.speed = speed
        self.color = color
        self.len = 40
        self.direction = 'RIGHT'
        self.KEYPULL = shoot

    def draw(self):
        tank_pos = (self.x + int(self.len / 2), self.y + int(self.len / 2))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.len, self.len), 5)

        if self.direction == 'UP':
            pygame.draw.line(window, self.color, tank_pos, (self.x + int(self.len / 2), self.y - int(self.len / 2)), 10)

        if self.direction == 'DOWN':
            pygame.draw.line(window, self.color, tank_pos, (self.x + int(self.len / 2), self.y + self.len + int(self.len / 2)), 10)

        if self.direction == 'RIGHT':
            pygame.draw.line(window, self.color, tank_pos, (self.x + self.len + int(self.len / 2), self.y + int(self.len / 2)), 10)

        if self.direction == 'LEFT':
            pygame.draw.line(window, self.color, tank_pos, (self.x - int(self.len / 2), self.y + int(self.len / 2)), 10)



    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == 'LEFT':
            self.x -= self.speed
        if self.direction == 'RIGHT':
            self.x += self.speed
        if self.direction == 'UP':
            self.y -= self.speed
        if self.direction == 'DOWN':
            self.y += self.speed
        self.draw()
    
class Bull:
    def __init__(self,x=0,y=0,color=(0,0,0),direction='LEFT',speed=7):
        self.x=x
        self.y=y
        self.color=color
        self.speed=speed
        self.direction=direction
        self.status=True
        self.distance=0
        self.radius=10

    def move(self):
        if self.direction == 'LEFT':
            self.x -= self.speed
        if self.direction == 'RIGHT':
            self.x += self.speed
        if self.direction == 'UP':
            self.y -= self.speed
        if self.direction == 'DOWN':
            self.y += self.speed
        self.distance += 1
        self.draw()

    def draw(self):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)

def buhhh(tank):
    if tank.direction == 'RIGHT':
        x = tank.x + tank.len + tank.len // 2
        y = tank.y + tank.len // 2

    if tank.direction == 'LEFT':
        x = tank.x - tank.len // 2
        y = tank.y + tank.len // 2

    if tank.direction == 'UP':
        x = tank.x + tank.len // 2
        y = tank.y - tank.len // 2

    if tank.direction == 'DOWN':
        x = tank.x + tank.len // 2
        y = tank.y + tank.len + tank.len // 2

    p = Bull(x, y, black, tank.direction)
    pulya.append(p)

def boom():
    if tanks[0].x < 0 or tanks[0].x > size_x - 20: #granica
        game_over()
    if tanks[0].y < 0 or tanks[0].y > size_y - 20:
        game_over()
    for p in pulya:
        if p.x < 0 or p.x > size_x - 20: #granica
            pulya.remove(p)
        if p.y < 0 or p.y > size_y - 20: #granica
            pulya.remove(p)

def game_over():
    pygame.mixer.music.stop()
    game_overSound.play()
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Good Bye!', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size_x//2, size_y//4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

tank1 = Tank(160, 120, 3, (43, 68, 51), shoot=pygame.K_SPACE)

bullet1 = Bull()


tanks = [tank1]
pulya = [bullet1]

clock = pygame.time.Clock()

black = pygame.Color(0, 0, 0)
white = pygame.Color(250, 250, 200)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

while True:
    clock.tick(30)
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over()
            pressed = pygame.key.get_pressed()
            for tank in tanks:
                if event.key in Directions.keys():
                    tank.change_direction(Directions[event.key])
                
                if pressed[tank.KEYPULL]:
                    bulletSound.play()
                    buhhh(tank)

    for tank in tanks:                   
        tank.move()

    for p in pulya:
        p.move()
    
    for tank in tanks:
        tank.draw() 

    boom()
    
    pygame.display.flip()

pygame.quit()