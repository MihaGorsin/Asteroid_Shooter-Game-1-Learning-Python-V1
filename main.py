import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')
clock = pygame.time.Clock()

# importing images 
ship_surf = pygame.image.load('./Grafike/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))
bg_surf = pygame.image.load('./Grafike/background.png').convert()
# 1. import the laser surface and create rect
# 2. rect start pos -> at the top mid of the ship
laser_surface = pygame.image.load('./Grafike/laser.png').convert_alpha()
laser_rect = laser_surface.get_rect(midbottom = ship_rect.midtop)

# import text 
font = pygame.font.Font('./Grafike/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

def get_laser_pos():
    laser_rect_zacetek = pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


	# framerate limit
    clock.tick(120)

    # mouse input position
    ship_rect.center = pygame.mouse.get_pos()
    
    laser_rect.y -= 10

    if event == pygame.MOUSEBUTTONDOWN:
        laser_rect.center = pygame.mouse.get_pos()
        laser_rect.y = 0



    


	# 2. updates 
    display_surface.fill((0, 0, 0)) 
    display_surface.blit(bg_surf,(0,0))
    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,text_rect)
    display_surface.blit(laser_surface, laser_rect)

    


	# 3. show the frame to the player / update the display surface
    pygame.display.update()