import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()

FPS = 2
WIDTH = 800
HEIGHT = 600
MAXRADIUS = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global score
score = 0

font = pygame.font.SysFont("comicsansms", 32)
#font = pygame.font.Font(Nont, 32)

def new_ball():
    '''рисует новый шарик '''
    global x,y, r
    x = randint(MAXRADIUS, WIDTH-MAXRADIUS)
    y = randint(MAXRADIUS, HEIGHT-MAXRADIUS)
    r = randint(10, MAXRADIUS)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    global score
    distance = math.hypot(event.pos[0] - x, event.pos[1] - y)
    if distance < r:
        #print('Hit')
        score = score + 1

def draw_score():
    text = font.render("Score: " + str(score), True, (0, 255, 0))
    screen.blit(text, (WIDTH - text.get_width(), 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    new_ball()
    draw_score()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
