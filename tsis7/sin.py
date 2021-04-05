import pygame
import math
pygame.init()

size = (700, 500)

screen = pygame.display.set_mode(size)
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
screen.fill(WHITE)
PI = 3.14

done = False
x1 = -PI*2
y1 = 250 + math.sin(x1) *150
a1 = x1
b1 = y1

x2 = -PI*2
y2 = 250 + math.cos(x2) *150
a2 = x2
b2 = y2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x1 = round(x1)
    x2 = round(x2)

    pygame.draw.line(screen, BLACK, [0, 250], [700, 250], 1)
    pygame.draw.line(screen, BLACK, [350 - (3*PI), 0], [350 - (3*PI), 500], 1)


    pygame.draw.aalines(screen, (225, 10, 10), True, [(a1, b1), (x1, y1)], 1)
    pygame.draw.aalines(screen, (10, 10, 225), True, [(a2, b2), (x2, y2)], 1)
    a1 = x1
    b1 = y1
    y1 = 250
    x1 += PI*2
    y1 += math.sin(x1) *150

    a2 = x2
    b2 = y2
    y2 = 250
    x2 += PI*2
    y2 += math.cos(x2) *150
 
    pygame.display.flip()

pygame.quit() 
