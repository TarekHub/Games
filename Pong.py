import pygame

def restart_Game():
    global  x_ball, y_ball
    x_ball = 200
    y_ball = 100


BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0,  255, 0]

TAILLECRAN = [400, 400]
# init
pygame.init()

_surface = pygame.display.set_mode(TAILLECRAN)
pygame.display.set_caption("Pong - by Tarek")

clock = pygame.time.Clock()

x_ball = 200
y_ball = 100

p1x = 0
p1y = 0

p2x = 400
p2y = 0

dx = 2
dy = 2

Ball_Radius = 5
Palet_length = 50

Score_P1 = 0
Score_P2 = 0

reglage_Display = 15

Close = False

while not Close:
    # Subscribe to Events
    events = pygame.event.Event(pygame.USEREVENT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p2y -= 20
            if event.key == pygame.K_DOWN:
                p2y += 20
            if event.key == pygame.K_z:
                p1y -= 20
            if event.key == pygame.K_s:
                p1y += 20

    # Logic :

    # Deplacement des palets:

    if p1y < 0:
        p1y = 0
    if p1y > TAILLECRAN[1] - Palet_length:
        p1y = TAILLECRAN[1] - Palet_length

    if p2y < 0:
        p2y = 0
    if p2y > TAILLECRAN[1] - Palet_length:
        p2yy = TAILLECRAN[1] - Palet_length

    # Deplacement ordinare de la boule
    x_ball += dx
    y_ball += dy

    # Les types de Repond
    if p1x + reglage_Display > x_ball - Ball_Radius  and y_ball in range(p1y, p1y + Palet_length):
        dx *= -1
    if x_ball + Ball_Radius > p2x - reglage_Display and y_ball in range(p2y, p2y + Palet_length):
        dx *= -1

    if y_ball < 0 or y_ball > TAILLECRAN[1] :
        dy *= -1

    if x_ball < 0:
        Score_P2 += 1
        restart_Game()
    if x_ball > TAILLECRAN[0]:
        Score_P1 += 1
        restart_Game()

    """
    if y_ball > TAILLECRAN[1]:
        if dx < 0:
            print("User 1 won !")
        else:
            print("User 2 won !")
    """

    #Display
    _surface.fill(BLACK)

    # dessiner la boule
    pygame.draw.circle(_surface, WHITE, [x_ball, y_ball], Ball_Radius * 2)

    # dessine les 2 palet de jeu
    pygame.draw.line(_surface, width=10, color=WHITE, start_pos=[p1x, p1y], end_pos=[p1x, p1y + Palet_length])
    pygame.draw.line(_surface, width=10, color=WHITE, start_pos=[p2x, p2y], end_pos=[p2x, p2y + Palet_length])

    font = pygame.font.Font('freesansbold.ttf', 40)
    text1 = font.render(f"{Score_P1}", True, GREEN)
    text2 = font.render(f"{Score_P2}", True, GREEN)
    rect1 = text1.get_rect()
    rect2 = text2.get_rect()
    rect1.topright = (TAILLECRAN[0] / 2  - 20, 5)
    rect2.topleft = (TAILLECRAN[0] / 2 + 20 , 5)

    _surface.blit(text1, rect1)
    _surface.blit(text2, rect2)

    clock.tick(30)
    pygame.display.flip()


pygame.quit()