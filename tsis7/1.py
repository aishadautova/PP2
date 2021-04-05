import pygame

pygame.init()
size = width, height = (400, 300)

screen = pygame.display.set_mode(size)

screen.fill((0,0,0))

pygame.draw.rect(screen, (180, 70, 80), (20, 30, 100, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.flip()
