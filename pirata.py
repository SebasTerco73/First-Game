import pygame

pygame.init()
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
print(f'{height} - {width}')
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pirata del caribe")
back = 1
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Pa Arriba")
                back = 1
            if event.key == pygame.K_DOWN:
                print("Pa Abajo")
                back = 1
            if event.key == pygame.K_LEFT:
                print("Pa Izq")
                back = 1
            if event.key == pygame.K_RIGHT:
                print("Pa Der")
                back = 1
            if event.key == pygame.K_SPACE:
                if back == 3:
                    jugando = False
                else:
                    back +=1
            if event.key == pygame.K_ESCAPE:
                jugando = False
            
pygame.quit()




    