import copy
import os
import copy as co
import pygame
from pygame import mixer

import numpy as np
from numpy.random import randint

# region colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
# endregion
Height = 500
Width = 500
Cadre = 60
pat = 3
TAILLE_ECRAN = [Width, Height]
deltaX = [-pat, pat, 0]
deltaY = [-pat, pat, 0]

# Init pygame

pygame.init()
mixer.init()
mixer.music.load('./resources/sond.mp3')
mixer.music.set_volume(0.7)


_surface = pygame.display.set_mode(TAILLE_ECRAN)
pygame.display.set_caption("Rock-Paper-Scissors - by Tarek")
clock = pygame.time.Clock()

# Variables du jeux

paper = pygame.image.load(os.path.join('./resources/ICONS', 'old-paper.png'))
rock = pygame.image.load(os.path.join('./resources/ICONS', 'rock.png'))
scissor = pygame.image.load(os.path.join('./resources/ICONS', 'scissors.png'))

listIcons = np.array([paper, rock, scissor], dtype=object)
nbrElement = 90

# Generating elements
listElements = np.zeros([90, 4], dtype=object)
for i in range(30):
    arr = np.array([randint(Cadre, Width-Cadre), randint(Cadre, Height - Cadre), "Paper", paper], dtype=object)
    listElements[i] = arr

for i in range(30, 60):
    arr = np.array([randint(Cadre, Width - Cadre), randint(Cadre, Height - Cadre), "Rock", rock], dtype=object)
    listElements[i] = arr

for i in range(60, 90):
    arr = np.array([randint(Cadre, Width - Cadre), randint(Cadre, Height - Cadre), "Scissor", scissor], dtype=object)
    listElements[i] = arr


Exit_Game = False

while not Exit_Game:
    # Events
    event = pygame.event.Event(pygame.USEREVENT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit_Game = True

    # Logic
    for element in listElements:
        dX = np.random.choice(deltaX)
        dY = np.random.choice(deltaY)
        element[0] = element[0] + dX
        element[1] = element[1] + dY
    # Rebond
    for element in listElements:
        if element[0] > Height - Cadre:
            element[0] = element[0] - 5
        if element[0] < Cadre:
            element[0] = element[0] + 5

        if element[1] > Width - Cadre:
            element[1] = element[1] - 5
        if element[1] < Cadre:
            element[1] = element[1] + 5
    # Collision
    for i in range(len(listElements)):
        current_element = listElements[i]
        for j in range(i + 1, len(listElements)):
            other_element = listElements[j]
            if abs(current_element[0] - other_element[0]) < 10 and abs(current_element[1] - other_element[1]) < 10:

                if current_element[2] == "Paper":
                    if other_element[2] == "Rock":
                        other_element[2] = "Paper"
                        other_element[3] = co.copy(current_element[3])
                        mixer.music.play()
                    elif other_element[2] == "Scissor":
                        current_element[2] = "Scissor"
                        current_element[3] = co.copy(other_element[3])
                        mixer.music.play()


                elif current_element[2] == "Rock":
                    if other_element[2] == "Scissor":
                        other_element[2] = "Rock"
                        other_element[3] = co.copy(current_element[3])
                        mixer.music.play()

                    elif other_element[2] == "Paper":
                        current_element[2] = "Paper"
                        current_element[3] = co.copy(other_element[3])
                        mixer.music.play()


                else:
                    if other_element[2] == "Paper":
                        other_element[2] = "Scissor"
                        other_element[3] = co.copy(current_element[3])
                        mixer.music.play()

                    elif other_element[2] == "Rock":
                        current_element[2] = "Rock"
                        current_element[3] = co.copy(other_element[3])
                        mixer.music.play()

    # Poursuite



    # Display
    _surface.fill(WHITE)

    for element in listElements:
        _surface.blit(element[3], (element[0], element[1]))

    clock.tick(14)
    pygame.display.flip()
pygame.quit()
