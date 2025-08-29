import pygame

ROJO = (255,0,0)
AMARILLO = (255,255,0)
VERDE = (0,255,0)

pygame.init()
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
print(f'{width} - {height}')
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pirata del caribe")
back = 1
jugando = True
while jugando:
    pygame.draw.circle(screen,ROJO,(100,500), 60)
    pygame.draw.circle(screen,(50,50,0),(100,300), 60)
    pygame.draw.circle(screen,(0,50,0),(100,100), 60)
    
    pygame.draw.circle(screen,(50,0,0),(300,500), 60)
    pygame.draw.circle(screen,AMARILLO,(300,300), 60)
    pygame.draw.circle(screen,(0,50,0),(300,100), 60)
    
    pygame.draw.circle(screen,(50,0,0),(500,500), 60)
    pygame.draw.circle(screen,(50,50,0),(500,300), 60)
    pygame.draw.circle(screen,VERDE,(500,100), 60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Pa Arriba")
                back = 1
            
            if event.key == pygame.K_ESCAPE:
                #sys.exit()
                jugando = False
            
pygame.quit()

