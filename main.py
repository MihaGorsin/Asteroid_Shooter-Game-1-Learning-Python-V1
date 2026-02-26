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

#Rabiš convertat v convert ali convert alpha
ship_surf = pygame.image.load('./Grafike/Ladja-1.png').convert_alpha()
ozadje = pygame.image.load('./Grafike/Ozadje.png').convert()


# Test animacije ladje
x_za_ladjo = 700

while True: # To bo v neskončnost loopalo

    # 1. input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Frame limit
    clock.tick(60)

    # 2. updates
    display_surface.fill('dark gray')
    display_surface.blit(ozadje)
    x_za_ladjo -= 1 
    display_surface.blit(ship_surf,(300,x_za_ladjo))
    display_surface.blit(text_surf,((WINDOW_WIDTH /2) - 40 ,10))
    
    

    # 3.show the frame to the player / update the display surface
    pygame.display.update()

