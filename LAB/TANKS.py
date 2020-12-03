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

boomSound = pygame.mixer.Sound('boom.wav')
bulletSound = pygame.mixer.Sound('bullet.wav')
game_overSound = pygame.mixer.Sound('game_over.wav')

Directions1 = {
    pygame.K_d: 'RIGHT', 
    pygame.K_a: 'LEFT',
    pygame.K_w: 'UP', 
    pygame.K_s: 'DOWN'
}
Directions2 = {
    pygame.K_RIGHT: 'RIGHT', 
    pygame.K_LEFT: 'LEFT',
    pygame.K_UP: 'UP', 
    pygame.K_DOWN: 'DOWN'
}

class Tank:
    def __init__(self, x, y, speed, color, shoot):
        self.x = x
        self.y = y
        self.score = 0
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
    def __init__(self, x = 0, y = 0, color = (0, 0, 0), direction='LEFT', speed=7):
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

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(tanks[0].score) + ' : ' + str(tanks[1].score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (size_x // 2, 10)
    elif choice == 2:
        score_rect.midtop = (size_x // 2 , size_y // 1.25)
    window.blit(score_surface, score_rect)



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

    bullet = Bull(x, y, black, tank.direction)
    bullets.append(bullet)

def win(w):
    my_font = pygame.font.SysFont('times new roman', 90)
    if w == 1:
        game_over_surface = my_font.render('WIN tank1', True, (255 - 86, 255 - 136, 255 - 102))
    else:
        game_over_surface = my_font.render('WIN tank2', True, (43, 68, 51))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size_x//2, size_y//4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def boom():
    for bullet in bullets:
        for tank in tanks:
            if(tank.x + tank.len + bullet.radius > bullet.x > tank.x - bullet.radius ) and ((tank.y + tank.len + bullet.radius > bullet.y > tank.y - bullet.radius)) and bullet.status==True:
                boomSound.play()
                bullets.remove(bullet)
                tank.score += 1
                bullet.status=False
                
                tank.x=random.randint(20, size_x - 20)
                tank.y=random.randint(20, size_y - 20)
    if(tanks[0].score - tanks[1].score >= 3):
        win(1)
    if(tanks[1].score - tanks[0].score >= 3):
        win(2)        
    # if tanks[0].x < 0 or tanks[0].x > size_x - 20: #granica
    #     win(2)
    # if tanks[0].y < 0 or tanks[0].y > size_y - 20:
    #     win(2)
    # if tanks[1].x < 0 or tanks[1].x > size_x - 20: #granica
    #     win(1)
    # if tanks[1].y < 0 or tanks[1].y > size_y - 20:
    #     win(1)

    for tank in tanks:
        if tank.x < -41:
            tank.x = size_x
        elif tank.x > size_x:
            tank.x = -40
        if tank.y < -41:
            tank.y = size_y
        elif tank.y > size_y:
            tank.y = -40

    for bullet in bullets:
        if bullet.x < 0 or bullet.x > size_x - 20: #granica
            bullets.remove(bullet)
        if bullet.y < 0 or bullet.y > size_y - 20: #granica
            bullets.remove(bullet)

def game_over():
    pygame.mixer.music.stop()
    game_overSound.play()
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Good Bye!', True, red)
    show_score(2, white, 'times', 20)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size_x//2, size_y//4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

tank1 = Tank(160, 120, 3, (43, 68, 51), shoot=pygame.K_SPACE)
tank2 = Tank(size_x - 160, size_y - 120, 3, (255 - 86, 255 - 136, 255 - 102), shoot=pygame.K_m)
bullet1 = Bull()
bullet2 = Bull()

tanks = [tank1, tank2]
bullets = [bullet1, bullet2]

clock = pygame.time.Clock()

black = pygame.Color(0, 0, 0)
white = pygame.Color(250, 250, 200)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

while True:
    clock.tick(30)
    window.fill(white)
    show_score(1, black, 'times', 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over()
            pressed = pygame.key.get_pressed()
            # for tank in tanks:
            if event.key in Directions1.keys():
                tanks[0].change_direction(Directions1[event.key])
            if pressed[tanks[0].KEYPULL]:
                bulletSound.play()
                buhhh(tanks[0])
            if event.key in Directions2.keys():
                tanks[1].change_direction(Directions2[event.key])
            if pressed[tanks[1].KEYPULL]:
                bulletSound.play()
                buhhh(tanks[1])

    for tank in tanks:                   
        tank.move()

    for bullet in bullets:
        bullet.move()
    
    for tank in tanks:
        tank.draw() 

    boom()
    
    pygame.display.flip()

pygame.quit()