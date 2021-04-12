import pygame, random

def main():
    screen = pygame.display.set_mode((800, 600))
    mode = 'random'
    draw_on = False
    lasr_pos = (0, 0)
    color = (225, 128, 0)
    radius = 10

    colors = {
        'red': (225, 0, 0),
        'blue': (0, 0, 225),
        'green': (0, 225, 0)
    }

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
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
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors(mode)
                
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    pygame.draw.circle(screen, color, event.pos, radius)
                #last.pos = event.pos
        
        pygame.display.flip()
    
    pygame.quit()

main()
