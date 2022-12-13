import copy
import random
import sys

import pygame

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0,  255, 0]
RED = [255, 0, 0]


Height = 400
Width = 400
TAILLE_ECRAN=[Width, Height]

pixels_by_square = 10
Grid_Height = 40
Grid_Width = 40

pygame.init()
_surface = pygame.display.set_mode(TAILLE_ECRAN)
pygame.display.set_caption("Snake - by Tarek")

clock = pygame.time.Clock()

# Initialisation état Initial des variables du Jeux

x_Head_Snake = 35
y_Head_Snake = 35

x_previous = x_Head_Snake
y_previous = y_Head_Snake

x_Poit = random.randint(0, Grid_Width - 1)
y_Poit = random.randint(0, Grid_Height - 1)

Snake = [[x_previous, y_previous + 1], [x_previous, y_previous + 2],
         [x_previous, y_previous + 3], [x_previous, y_previous + 4]]

Grille = []
Score = 0
Last = 0
Head_Color = GREEN

direction = "up"

for x in range(Grid_Height):
    L = []
    for y in range(Grid_Width):
        L.append(0)
    Grille.append(L)

Exit_Game = False

# region Functions

def follow_the_lead():
    global Last
    for i in range(len(Snake)):
        if i == 0:
            # for the 1st square of the snake
            Last = copy.copy(Snake[i])
            Snake[i][0] = x_previous
            Snake[i][1] = y_previous
        else:
            # get coordinates from the past square
            mid = copy.copy(Snake[i])
            Snake[i] = Last
            Last = mid

def set_previous():
    global x_previous, y_previous
    x_previous = x_Head_Snake
    y_previous = y_Head_Snake

def add_Squre():
    global Snake
    Snake.append(Last)

def game_Over():
    ...

# endregion

while not Exit_Game:
    # Catch Events // Subscription
    events = pygame.event.Event(pygame.USEREVENT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_previous != y_Head_Snake - 1:
                    direction = "up"

            if event.key == pygame.K_DOWN:
                if y_previous != y_Head_Snake + 1:
                    direction = "down"

            if event.key == pygame.K_LEFT:
                if x_previous != x_Head_Snake - 1:
                    direction = "left"

            if event.key == pygame.K_RIGHT:
                if x_previous != x_Head_Snake + 1:
                    direction = "right"


    # Logic

    # When the snake collide with himself
    for element in Snake:
        if x_Head_Snake == element[0]  and y_Head_Snake == element[1]:
            Head_Color = RED
            direction = "stop"

    # Direction movement
    if direction == "up":
        set_previous()
        y_Head_Snake -= 1
        follow_the_lead()
    elif direction == "down":
        set_previous()
        y_Head_Snake += 1
        follow_the_lead()
    elif direction == "right":
        set_previous()
        x_Head_Snake += 1
        follow_the_lead()
    elif direction == "left":
        set_previous()
        x_Head_Snake -= 1
        follow_the_lead()
    elif direction == "stop":
        x_Head_Snake = x_Head_Snake

    # When snake reaches borders
    if x_Head_Snake < 0 or x_Head_Snake >= Grid_Width :
        x_Head_Snake = x_Head_Snake % (Width / pixels_by_square)
    if y_Head_Snake < 0 or y_Head_Snake >= Grid_Height :
        y_Head_Snake = y_Head_Snake % (Height / pixels_by_square)

    # When eating the point
    if x_Head_Snake == x_Poit and y_Head_Snake == y_Poit:
        Score += 1
        add_Squre()
        x_Poit = random.randint(0, Grid_Width -1)
        y_Poit = random.randint(0, Grid_Height -1)


    # Display

    _surface.fill(BLACK)

    x0 = x_Head_Snake * pixels_by_square
    y0 = y_Head_Snake * pixels_by_square

    # Movement Head Snake
    head = pygame.draw.rect(_surface, Head_Color, pygame.Rect(x0, y0, pixels_by_square, pixels_by_square))
    # The Rest
    for square in Snake:
        x0 = square[0] * pixels_by_square
        y0 = square[1] * pixels_by_square
        pygame.draw.rect(_surface, WHITE, pygame.Rect(x0, y0, pixels_by_square, pixels_by_square))

    # The Poit
    x_Circle = x_Poit * pixels_by_square
    y_Circle = y_Poit * pixels_by_square
    point = pygame.draw.circle(_surface, GREEN, [x_Circle + 5, y_Circle + 5], 5)

    # Score
    font = pygame.font.Font('C:\\Users\\acer\\Desktop\\Code\\Python\\Games\\resources\\Inconsolata-Regular.ttf', 20)
    score = font.render(f"Score : {Score}", True, WHITE)
    rect1 = score.get_rect()
    rect1.topleft = 20, 20
    _surface.blit(score, rect1)


    clock.tick(10)
    pygame.display.flip()

pygame.quit()

