import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
surf = pygame.Surface((150, 150))
surf.fill((100, 150, 0))
pygame.draw.rect(surf, (10, 100, 200), (10, 10, 40, 40))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(surf, (50, 20))
    pygame.display.flip()

pygame.quit()