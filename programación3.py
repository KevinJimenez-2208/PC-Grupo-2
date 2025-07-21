#Básico (Desplegar la pantalla)
import pygame
pygame.init
screen = pygame.display.set_mode((740, 740))


running = True

clock = pygame.time.Clock()

while running:

    screen.fill((34,217,238))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()

