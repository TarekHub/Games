# permet d'accéder aux fonctions du module pygame
import pygame
import random

# Definit des couleurs RGB
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
YELLOW = [255,255,0]
RED = [255, 0, 0]
BLUE = [0 , 0 , 255]

# initialisation de l'écran de jeu
pygame.init()
police = pygame.font.SysFont("Arial", 25)

# Initialise la fenêtre de jeu
TailleEcran = [500, 500]
screen = pygame.display.set_mode(TailleEcran)
pygame.display.set_caption("Snake")

# Gestion du rafraichissement de l'écran
clock = pygame.time.Clock()

SCORE = 0
# Position de départ
LARG = 10
Snake1 = []
for x in range(10):
  Snake1.append([x+10,10])

PomXY = [20,20]

Acceleration = 10

# Vitesse et direction
dirS1 = [1,0]

def DessineCase(P,coul):
    x,y = P
    x *= LARG
    y *= LARG
    pygame.draw.rect(screen,coul,[x,y,LARG,LARG])


# Le jeu continue tant que l'utilisateur ne ferme pas la fenêtre
Termine = False
comptage = 0

# BOUCLE PRINCIPALE DU PROGRAMME
while not Termine:
  comptage += 1
  SCORE += 1
  # recupère la liste des évènements du joueur
  event = pygame.event.Event(pygame.USEREVENT)

  # EVENEMENTS
  # détecte le clic sur le bouton close de la fenêtre
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Termine = True

   # récupère la liste des touches claviers appuyeées sous la forme d'une liste de booléens
  KeysPressed = pygame.key.get_pressed()

  # LOGIQUE
  fillcoul = BLACK


  # LOGIQUE
  # touches déplacement
  if KeysPressed[pygame.K_LEFT]:
      dirS1 = [-1,0]
  if KeysPressed[pygame.K_RIGHT]:
      dirS1 = [1,0]
  if KeysPressed[pygame.K_UP]:
      dirS1 = [0,-1]
  if KeysPressed[pygame.K_DOWN]:
      dirS1 = [0,1]

  # Déplace le serpent
  if comptage % Acceleration == 0 :
    TETE = Snake1[-1]
    nextMove = [ (TETE[0]+dirS1[0])%50, (TETE[1]+dirS1[1])%50 ]
    Snake1.append(nextMove)
    Snake1.pop(0)

  # detecte la collision avec lui même
  TETE = Snake1[-1]
  if Snake1.count(TETE) > 1 :
    fillcoul = RED
    SCORE -= 100

  # detecte la collision avec la pomme
  if TETE == PomXY :
    xx = random.randint(0,49)
    yy = random.randint(0,49)
    PomXY = [xx,yy]
    SCORE += 5000
    # allonge le serpent
    QUEUE = Snake1[0]
    Snake1.insert(0,QUEUE)
    Snake1.insert(0,QUEUE)
    Snake1.insert(0,QUEUE)
    # on augmente la vitesse
    Acceleration = max(2,Acceleration-1)


  # AFFICHAGE
  # Dessine le fond
  screen.fill(fillcoul)

  # serpent1
  for s in Snake1 :
     DessineCase(s,YELLOW)
  Tete = Snake1[-1]
  DessineCase(Tete,WHITE)

  #pomme
  DessineCase(PomXY,GREEN)

  #  dessine le texte dans une zone de rendu à part
  zone = police.render( str(SCORE), True, GREEN)
  # affiche la zone de rendu au dessus de fenetre de jeu
  screen.blit(zone,(240,10))


  # Demande à pygame de se caler sur 30 FPS
  clock.tick(30)

  # Bascule l'image dessinée à l'écran
  pygame.display.flip()



# Ferme la fenêtre
del(police)
pygame.quit()
