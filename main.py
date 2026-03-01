import pygame, sys #sistem smo importali, da lahko celo zadevo uganemo

# Vse pygame sisteme moramo zagnati
pygame.init()
# Nastavimo širino in višino ekrana
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
# nastavimo velikost okna programa
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Ime, ki bo na okviru okna
pygame.display.set_caption('Neteor shooter')


#za FPS
clock = pygame.time.Clock()

# Surface je grafična površina
#test_surface = pygame.Surface((400,100))
# Surface rabimo pritrditi na display surface

# import font
font = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 50)
# Ta false je aa antyaliesing ali nekiaj - gre za robove
text_surf = font.render('Ladja', False, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 80))

#Rabiš convertat v convert ali convert alpha
ship_surf = pygame.image.load('./Grafike/Ladja-1.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
print(ship_rect)

ozadje = pygame.image.load('./Grafike/Ozadje.png').convert()

smer_premika = 3
# Test animacije ladje


while True: # To bo v neskončnost loopalo

    # 1. input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ship_rect.x -= smer_premika
    if ship_rect.x < 0:
        smer_premika = -3

    if ship_rect.x > 350:
        smer_premika = 3
    # Frame limit
    clock.tick(60)



    # 2. updates
    display_surface.fill('dark gray')
    display_surface.blit(ozadje)
    display_surface.blit(ship_surf,(ship_rect))
    display_surface.blit(text_surf,text_rect)
    
    

    # 3.show the frame to the player / update the display surface
    pygame.display.update()

