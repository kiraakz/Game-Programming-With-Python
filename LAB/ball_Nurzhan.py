import pygame
import random
import time
import sys

pygame.init()
win = pygame.display.set_mode((500, 500)) 

pygame.display.set_caption("Ball")
bg = pygame.image.load('ball_Nurzhan.jpg')

pygame.mixer.music.load('nurzh.mp3')
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
size_x = 500
size_y = 500

x = 50
y = 430
w = 80
h = 20
speed = 5

isJump = False
jumpcount = 10

left = False
right = False

animcount = 0

red = (255, 0, 0)
white = (255, 255, 255)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

cnt = 0

def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (500//2, 500//4)
    win.fill(black)
    win.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(cnt), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (50, 10)
    else:
        score_rect.midtop = (250 , int(500.0 // 1.25))
    win.blit(score_surface, score_rect)


class sn():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vel = 8

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)

lastmove = 'right'

run = True
def drawWindow():
    global animcount
    win.blit(bg, (0, 0))
    show_score(1, black, 'times', 20)

    for bullet in bullets:
        bullet.draw(win)
    pygame.draw.rect(win, (255, 0, 0), (x, y, w, h))

    pygame.display.update()


bullets = []

vel = 0
died = 0


while run:
    clock.tick(60)

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y < y + h and bullet.y > y and bullet.x < x + w and bullet.x > x:
            cnt += 1
            bullets.remove(bullet)
        if bullet.y < 500 and bullet.y > 0: 
            bullet.y += bullet.vel + vel
        else:
            died += 1
            bullets.remove(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    if len(bullets) < 5:
        bullets.append(sn(random.randrange(20, 480) // 10 * 10, 10, 10, (18, 5, 71)))

    if died == 10:
        game_over()

    if cnt == 20:
        vel += 1
        speed += 1

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - w - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animcount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]: isJump = True
    else:
        if jumpcount >= -10:
            if(jumpcount < 0):
                y += (jumpcount**2) / 2
            else:
                y -= (jumpcount**2) / 2
            jumpcount -= 1
        else:
            isJump = False
            jumpcount = 10
    

    print(cnt)
    drawWindow()


pygame.quit()