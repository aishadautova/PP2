import pygame

pygame.display.set_mode((600, 400))
pygame.display.set_caption("Моя программа")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                quit()