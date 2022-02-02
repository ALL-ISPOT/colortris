import pygame
import colortris

pygame.init()

screen = pygame.display.set_mode(colortris.res)

def credits():
    screen.fill((0, 0, 20))
    credits_image = pygame.image.load('credits_final.png')
    screen.blit(credits_image, (0, 0))
    while(True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
        pygame.display.update()

mouse_over_color = (100, 100, 100)

def over_exit():
    pygame.draw.rect(screen, mouse_over_color, [260, 445, 120, 50], 5)

def over_start():
    pygame.draw.rect(screen, mouse_over_color, [260, 300, 145, 50], 5)

def over_credits():
    pygame.draw.rect(screen, mouse_over_color, [260, 375, 200, 50], 5)

while (True):
                
    screen.fill((0,0,20))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # exit
            if pos[0] > 260 and pos[0] < 375 and \
               pos[1] > 445 and pos[1] < 485:
                exit()
            # start
            if pos[0] > 260 and pos[0] < 405 and \
               pos[1] > 300 and pos[1] < 340:
                colortris.game_loop()
            # credits
            if pos[0] > 260 and pos[0] < 455 and \
               pos[1] > 375 and pos[1] < 415:
                credits()
        else:
            pos = pygame.mouse.get_pos()

            # over exit
            if pos[0] > 260 and pos[0] < 375 and \
               pos[1] > 445 and pos[1] < 485:
                over_exit()
            # over start
            if pos[0] > 260 and pos[0] < 405 and \
               pos[1] > 300 and pos[1] < 340:
                over_start()
            # over credits
            if pos[0] > 260 and pos[0] < 455 and \
               pos[1] > 375 and pos[1] < 415:
                over_credits()

    menu_image = pygame.image.load('menu.png')
    screen.blit(menu_image, (0, 0))
    
    color = (255, 255, 255)

    mb = pygame.mouse.get_pressed()

    if (mb[0]):
        color = (255, 0, 0)
    elif (mb[2]):
        color = (0, 255, 0)

    pos = pygame.mouse.get_pos()
    
    pygame.draw.circle(screen, color, pos, 20, 5)
    
    pygame.display.update()