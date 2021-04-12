import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400, 400))

class Food:
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)
    
    def gen(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)

    def draw(self):
        pygame.draw.rect(screen, (0, 225, 0), (self.x, self.y, 10, 10))

class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5 # right
        self.dy = 0
        self.is_add = False
        self.speed = 30
    
    # [x1, y1], [x2, y2], [x3, y3], [x4, y4] i -> i-1

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (225, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
    
    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx <= x <= foodx + 10 and foody <= y <= foody +10:
            return True
snake = Snake()
food = Food()
running = True

d = 5
FPS = 30

clock = pygame.time.Clock()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False
            
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d


    if snake.eat(food.x, food.y):
        snake.is_add = True
        food.gen()

    snake.move()
    screen.fill((0, 0, 0))
    snake.draw()
    food.draw()
    pygame.display.flip()

pygame.quit()