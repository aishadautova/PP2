import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
RED = (225, 0, 0)

size = (400, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyGame example")
PI = 3.14

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            done = True

    screen.fill(WHITE)
    # line
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    for y in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y], [100, 110 + y], 2)

    #rectangle
    pygame.draw.rect(screen, BLACK, [100, 100, 250, 100], 2)

    #ellipse
    pygame.draw.ellipse(screen, BLUE, [100, 200, 250, 100], 5)

    #arc
    pygame.draw.arc(screen, BLACK, [100, 100, 250, 100], 0, PI/2, 2)
    pygame.draw.arc(screen, GREEN, [100, 100, 250, 100], PI/2, PI, 2)
    pygame.draw.arc(screen, RED, [100, 100, 250, 100], PI, 3 * PI/2, 2)
    pygame.draw.arc(screen, BLUE, [100, 100, 250, 100], 3 * PI/2, PI * 2, 2)

    #text
    font = pygame.font.Font(None, 50)
    text1 = font.render("Help me", True, RED)
    text2 = font.render("Help me", False, RED)
    screen.blit(text1, (250, 300))
    screen.blit(text2, (250, 320))

    #text rotation
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Kogda eto zakonchitsya", True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (0, 0))

    pygame.display.flip()

pygame.quit() 