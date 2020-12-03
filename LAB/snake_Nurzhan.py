import pygame
import sys
import time
import random


pygame.init()
size_x = 800
size_y = 600
screen = pygame.display.set_mode((size_x, size_y))
done = False
is_blue = True
x = 10
y = 10

check_errors = pygame.init()

pygame.mixer.music.load('nurzh.mp3')
pygame.mixer.music.play(0)

pygame.display.set_caption('Snake')

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

clock = pygame.time.Clock()

snake_pos = [100, 50]
snake_size = [[100, 50], [90, 50], [80, 50]]

food_pos = [random.randrange(1, (size_x//10)) * 10, random.randrange(1, (size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

def game_over():
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    sys.exit()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            # Esc -> shygyp ketu
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= y
    if direction == 'DOWN':
        snake_pos[1] += y
    if direction == 'LEFT':
        snake_pos[0] -= x
    if direction == 'RIGHT':
        snake_pos[0] += x

    snake_size.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_size.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (size_x//10)) * 10, random.randrange(1, (size_y//10)) * 10]
    food_spawn = True

    screen.fill(black)

    for pos in snake_size:
        pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], x, y))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], x, y))

    if snake_pos[0] < 0 or snake_pos[0] > size_x-10: #granica
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > size_y-10:
        game_over()

    for block in snake_size[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]: #ozin zhep koymasa
            game_over()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(20)