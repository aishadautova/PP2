#q - Draw rectangle    c - Draw circle    rmb - Eraser    r, b, g - Color selection    z - Random color    s - Save picture

import pygame, random
import sys
pygame.init()

def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)

    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

def drawcircle(screen, color, pos1, pos2, pos3, pos4):
    if pos1 < pos3 and pos2 < pos4:
        pygame.draw.ellipse(screen, color, (pos1, pos2, pos3 - pos1, pos4 - pos2))
    if pos1 > pos3 and pos2 < pos4:
        pygame.draw.ellipse(screen, color, (pos3, pos2, pos1 - pos3, pos4 - pos2))
    if pos1 < pos3 and pos2 > pos4:
        pygame.draw.ellipse(screen, color, (pos1, pos4, pos3 - pos1, pos2 - pos4))
    if pos1 > pos3 and pos2 > pos4:
        pygame.draw.ellipse(screen, color, (pos3, pos4, pos1 - pos3, pos2 - pos4))

def drawrect(screen, color, pos1, pos2, pos3, pos4):

    if pos1 < pos3 and pos2 < pos4:
        pygame.draw.rect(screen, color, (pos1, pos2, pos3 - pos1, pos4 - pos2))
    if pos1 > pos3 and pos2 < pos4:
        pygame.draw.rect(screen, color, (pos3, pos2, pos1 - pos3, pos4 - pos2))
    if pos1 < pos3 and pos2 > pos4:
        pygame.draw.rect(screen, color, (pos1, pos4, pos3 - pos1, pos2 - pos4))
    if pos1 > pos3 and pos2 > pos4:
        pygame.draw.rect(screen, color, (pos3, pos4, pos1 - pos3, pos2 - pos4))

def t(screen):
    font = pygame.font.SysFont(None, 25)
    text = font.render("q - Draw rectangle    c - Draw circle    rmb - Eraser    r, b, g - Color selection    z - Random color    s - Save picture   up/down arrow - Size", True, (10, 10, 10))
    screen.blit(text, (0, 15))

def main():
    screen = pygame.display.set_mode((1200, 800))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10
    crl = False
    crl1 = False
    rect1 = False
    rect2 = False
    x, y = 0, 0
    black = (0, 0, 0)
    
    surf = pygame.Surface((1200, 50))
    surf.fill((200, 200, 200))

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    while True:

        screen.blit(surf, (0, 0))

        t(screen)

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_s:
                    pygame.image.save(screen, 'picture.png')

                if event.key == pygame.K_q:
                    rect1 = True
                
                if event.key == pygame.K_c:
                    crl = True

                if event.key == pygame.K_z:
                    mode = 'random'
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = pygame.mouse.get_pressed()
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                
                if rect1:
                    x, y = event.pos[0], event.pos[1]
                    rect2 = True
                
                elif crl:
                    x, y = event.pos[0], event.pos[1]
                    crl1 = True
                
                elif pressed[0]:
                    pygame.draw.circle(screen, color, event.pos, radius)
                    draw_on = True
                
                elif pressed[2]:
                    pygame.draw.circle(screen, black, event.pos, radius)
                    draw_on = True

            if event.type == pygame.MOUSEBUTTONUP:
                if crl1:
                    drawcircle(screen, color, x, y, event.pos[0], event.pos[1])

                if rect2:
                    drawrect(screen, color, x, y, event.pos[0], event.pos[1])
                crl = False
                crl1 = False
                rect1 = False
                rect2 = False
                draw_on = False

            if event.type == pygame.MOUSEMOTION:

                if draw_on:
                    pressed = pygame.mouse.get_pressed()

                    if pressed[2]:
                        drawLine(screen, last_pos, event.pos, radius, black)
                    if pressed[0]:
                        drawLine(screen, last_pos, event.pos, radius, color)

                last_pos = event.pos

        pygame.display.flip()

    pygame.quit()

main()