import pygame

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
BLUE = [0 , 0 , 255]

# initialisation de l'écran de jeu
pygame.init()

# Initialise la fenêtre de jeu
TailleEcran = [800, 600]
screen = pygame.display.set_mode(TailleEcran)
pygame.display.set_caption("Mega Ball")

# Gestion du rafraîchissement de l'écran
clock = pygame.time.Clock()

# Position de départ
balle_x = 0
balle_y = 300

# Vitesse et direction
balle_change_x = 3
balle_change_y = 3

# Couleur
Color = "red"

balle_rayon= 5

# Le jeu continue tant que l'utilisateur ne ferme pas la fenêtre
Termine = False

while not Termine:
    # recupère la liste des évènements du joueur -tous les évènements-
    event = pygame.event.Event(pygame.USEREVENT)

    # ÉVÈNEMENTS
    # détecte le clic sur le bouton close de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Termine = True

            # LOGIQUE
    # Déplace la balle
    balle_x += balle_change_x
    balle_y += balle_change_y

    # Rebond
    if balle_y > TailleEcran[1] or balle_y < 0:
        balle_change_y = balle_change_y * -1
        if Color == "red":
            Color="blue"
        else:
            Color= "red"
    if balle_x > TailleEcran[0] or balle_x < 0:
        balle_change_x = balle_change_x * -1
        if Color == "red":
            Color="blue"
        else:
            Color= "red"

        # AFFICHAGE
    # Dessine le fond
    screen.fill(BLACK)

    # Colorie les bords de l'écran
    R = [0, 0, TailleEcran[0], TailleEcran[1]]
    pygame.draw.rect(screen, GREEN, R, 5)

    # dessine le palet de jeu
    pygame.draw.circle(screen, BLUE, [balle_x, balle_y], balle_rayon * 4)
    pygame.draw.circle(screen, Color, [balle_x, balle_y], balle_rayon * 2)

    # Demande à Pygame de se caler sur 30 FPS
    clock.tick(60)

    # Bascule l'image dessinée à l'écran
    pygame.display.flip()

    # débogage
    print("position : " + str([balle_x, balle_y]))
    print("Dir : " + str([balle_change_x, balle_change_y]))

# Ferme la fenêtre
pygame.quit()