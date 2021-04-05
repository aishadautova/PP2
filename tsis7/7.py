import pygame
import random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
RED = (225, 0, 0)

size = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyGame example")
clock = pygame.time.Clock()

colors = [BLACK, BLUE, GREEN, RED]
color = BLACK

x = 100
y = 100
dx = 0
dy = 0

speed = 3

done = False
while not done:
    for event in pygame.event.get():
        while event.type == pygame.QUIT:  
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dx = 0
            dy = -1 * speed
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dx = 0
            dy = 1 * speed
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dx = 1 * speed
            dy = 0
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dx = -1 * speed
            dy = 0 
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed += 3

    
    screen.fill(WHITE)
    x += dx
    y += dy

    if x > 700:
        x = 0
    
    if x < 0:
        x = 700
    
    if y > 500:
        y = 0
    
    if y < 0:
        y = 500

    pygame.draw.ellipse(screen, color, [x, y, 20, 20])

    clock.tick(60)
    
    pygame.display.update()

pygame.quit() 