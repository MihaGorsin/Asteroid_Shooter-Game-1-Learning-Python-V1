import pygame, sys #sistem smo importali, da lahko celo zadevo uganemo

# Vse pygame sisteme moramo zagnati
pygame.init()
# Nastavimo širino in višino ekrana
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
# nastavimo velikost okna programa
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Ime, ki bo na okviru okna
pygame.display.set_caption('Neteor shooter')

# Surface je grafična površina
test_surface = pygame.Surface((400,100))
# Surface rabimo pritrditi na display surface

while True: # To bo v neskončnost loopalo

    # 1. input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. updates

    # 3.show the frame to the player / update the display surface
    pygame.display.update()

