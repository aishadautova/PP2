import pygame, time, pickle
import random, os
pygame.init()
screen = pygame.display.set_mode((400, 400))

f = open("size.txt", "w")
f.write('')
f.close()
f = open("scores.txt", "w")
f.write('')
f.close()
f = open("elements.txt", "w")
f.write('')
f.close()
safe = False

class Food:
    def __init__(self):
        self.x = random.randint(5, 395)
        self.y = random.randint(5, 395)
        
        if 55-5 <= self.x <= 85+5 and 95-5 <= self.y <= 355+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)
        if 175-5 <= self.x <= 405+5 and 175-5 <= self.y <= 205+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)
        if 295-5 <= self.x <= 325+5 and -5 <= self.y <= 75+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)
    
    def gen(self):
        self.x = random.randint(5, 395)
        self.y = random.randint(5, 395)

        if 55-5 <= self.x <= 85+5 and 95-5 <= self.y <= 355+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)
        if 175-5 <= self.x <= 405+5 and 175-5 <= self.y <= 205+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)
        if 295-5 <= self.x <= 325+5 and -5 <= self.y <= 75+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)

    def draw(self):

        if 55-5 <= self.x <= 85+5 and 95-5 <= self.y <= 355+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)
        if 175-5 <= self.x <= 405+5 and 175-5 <= self.y <= 205+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)
        if 295-5 <= self.x <= 325+5 and -5 <= self.y <= 75+5:
            self.x = random.randint(5, 395)
            self.y = random.randint(5, 395)

        pygame.draw.rect(screen, (0, 225, 0), (self.x, self.y, 10, 10))

class Snake:

    def __init__(self):

        if safe:
            f = open("size.txt", "rb")
            s = int(pickle.load(f))
            self.size = s
            f.close()

            f = open("elements.txt", "rb")
            s = list(pickle.load(f))
            self.elements = s
            f.close

        else:
            self.size = 1
            self.elements = [[200, 100]]
        
        self.radius = 10
        self.dx = 5 # right
        self.dy = 0
        self.is_add = False
        self.speed = 30
        self.lose = False

    def draw(self):

        for element in self.elements:
            pygame.draw.circle(screen, (225, 0, 0), element, self.radius)
            screen.blit(text, (3, 3))
            scores = font.render(str(SCORE1), True, (255, 255, 255))
            screen.blit(scores, (50, 4))

            if level2 or level3:
                pygame.draw.rect(screen, (120, 0, 0), (60, 100, 20, 250))
                pygame.draw.rect(screen, (120, 0, 0), (180, 180, 220, 20))
                pygame.draw.rect(screen, (120, 0, 0), (300, 0, 20, 70))

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

        x = self.elements[0][0]
        y = self.elements[0][1]
        if x > 400:
            self.elements[0][0] = 0
        if y > 400:
            self.elements[0][1] = 0
        if x < 0:
            self.elements[0][0] = 400
        if y < 0:
            self.elements[0][1] = 400
        
        if level2 or level3:
            if 60 <= x <= 80 and 100 <= y <= 350:
                LOSE()
                self.lose = True
            if 180 <= x <= 400 and 180 <= y <= 200:
                LOSE()
                self.lose = True
            if 300 <= x <= 320 and 0 <= y <= 70:
                LOSE()
                self.lose = True


    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx <= x <= foodx + 10 and foody <= y <= foody +10:
            return True

class Snake2:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx2 = 5 # right
        self.dy2 = 0
        self.is_add = False
        self.speed = 30

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (0, 0, 225), element, self.radius)
            screen.blit(text, (340, 3))
            scores = font.render(str(SCORE2), True, (255, 255, 255))
            screen.blit(scores, (385, 4))

    def add_to_snake2(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):

        if self.is_add:
            self.add_to_snake2()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        
        self.elements[0][0] += self.dx2
        self.elements[0][1] += self.dy2

        x = self.elements[0][0]
        y = self.elements[0][1]
        if x > 400:
            self.elements[0][0] = 0
        if y > 400:
            self.elements[0][1] = 0
        if x < 0:
            self.elements[0][0] = 400
        if y < 0:
            self.elements[0][1] = 400


    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx <= x <= foodx + 10 and foody <= y <= foody +10:
            return True

snake = Snake()
snake2 = Snake2()
food = Food()
running = True

d = 5
FPS = 30
clock = pygame.time.Clock()
level1 = False
level2 = False
level3 = False
play = False
pygame.draw.rect(screen, (220, 10, 60), (100, 60, 200, 50))
pygame.draw.rect(screen, (220, 10, 60), (100, 140, 200, 50))
pygame.draw.rect(screen, (220, 10, 60), (100, 220, 200, 50))
pygame.draw.rect(screen, (60, 10, 220), (100, 300, 200, 50))

font = pygame.font.Font(None, 20)
text = font.render("Score:", True, (255, 255, 255))
SCORE1 = 0
SCORE2 = 0
win = pygame.font.Font(None, 50)
text1 = win.render("WIN", True, (200, 25, 25))
text2 = win.render("GAME OVER", True, (200, 25, 25))
t1 = win.render("Easy", True, (200, 200, 200))
t2 = win.render("Medium", True, (200, 200, 200))
t3 = win.render("Hard", True, (200, 200, 200))
t4 = win.render("2 Players", True, (200, 200, 200))
screen.blit(t1, (159, 70))
screen.blit(t2, (135, 150))
screen.blit(t3, (160, 230))
screen.blit(t4, (125, 310))

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            x = A[0]
            y = A[1] 

            if 100 < x < 300 and 60 < y < 110:

                if os.path.getsize('scores.txt') != 0:
                    safe = True
                    f = open("scores.txt", "r")
                    A = f.read()
                    SCORE1 = int(A)
                
                screen.fill((0, 0, 0))
                level1 = True
            
            if 100 < x < 300 and 140 < y < 190:

                if os.path.getsize('scores.txt') != 0:
                    safe = True
                    f = open("scores.txt", "r")
                    A = f.read()
                    SCORE1 = int(A)

                screen.fill((0, 0, 0))
                level2 = True
            
            if 100 < x < 300 and 220 < y < 270:
                
                if os.path.getsize('scores.txt') != 0:
                    safe = True
                    f = open("scores.txt", "r")
                    A = f.read()
                    SCORE1 = int(A)

                screen.fill((0, 0, 0))
                level3 = True
            
            if 100 < x < 300 and 300 < y < 350:
                screen.fill((0, 0, 0))
                play = True
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                f = open("scores.txt", "w")
                s = str(SCORE1)
                f.write(s)

                f1 = open("elements.txt", "wb")
                s = str(snake.elements)
                pickle.dump(s, f1)
                
                f2 = open("size.txt", "wb")
                s = str(snake.size)
                pickle.dump(s, f2)

                f2.close()
                f1.close
                f.close()

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
            #second
            if event.key == pygame.K_d and snake2.dx2 != -d:
                snake2.dx2 = d
                snake2.dy2 = 0
            
            if event.key == pygame.K_a and snake2.dx2 != d:
                snake2.dx2 = -d
                snake2.dy2 = 0
            
            if event.key == pygame.K_w and snake2.dy2 != d:
                snake2.dx2 = 0
                snake2.dy2 = -d
            
            if event.key == pygame.K_s and snake2.dy2 != -d:
                snake2.dx2 = 0
                snake2.dy2 = d


    if snake.eat(food.x, food.y):
        if level3:
            d += 0.7
        SCORE1 += 1
        snake.is_add = True
        food.gen()
    
    if snake2.eat(food.x, food.y):
        if level3:
            d += 0.5
        SCORE2 += 1
        snake2.is_add = True
        food.gen()

    if play:
        snake2.move()
        snake.move()
        screen.fill((0, 0, 0))
        snake2.draw()
        snake.draw()
        food.draw()
    
    if level3:
        snake.move()
        screen.fill((0, 0, 0))
        snake.draw()
        food.draw()
    
    if level2:
        snake.move()
        screen.fill((0, 0, 0))
        snake.draw()
        food.draw()

    if level1:
        pygame.draw.ellipse(screen, (255, 255, 255), (10, 10, 20, 20), 3)
        snake.move()
        screen.fill((0, 0, 0))
        snake.draw()
        food.draw()
    
    if SCORE1 == 5 and not play:

        screen.fill((0, 0, 0))
        time.sleep(0.5)
        screen.blit(text1, (165, 180))
        pygame.display.update()
        time.sleep(1)

        d = 5
        snake.size = 1
        snake.elements.clear()
        snake.elements = [[200, 100]]
        screen.fill((0, 0, 0))
        SCORE1 = 0
        snake.dx = d
        snake.dy = 0
        level1 = False
        level2 = False
        level3 = False
        pygame.draw.rect(screen, (220, 10, 60), (100, 60, 200, 50))
        pygame.draw.rect(screen, (220, 10, 60), (100, 140, 200, 50))
        pygame.draw.rect(screen, (220, 10, 60), (100, 220, 200, 50))
        pygame.draw.rect(screen, (60, 10, 220), (100, 300, 200, 50))
        screen.blit(t1, (159, 70))
        screen.blit(t2, (135, 150))
        screen.blit(t3, (160, 230))
        screen.blit(t4, (125, 310))
        

    if play:
        if SCORE1 == 5:
            screen.fill((0, 0, 0))
            time.sleep(0.5)
            t = win.render("Player1 WIN", True, (200, 25, 25))
            screen.blit(t, (100, 180))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
        
        if SCORE2 == 5:
            screen.fill((0, 0, 0))
            time.sleep(0.5)
            t = win.render("Player2 WIN", True, (25, 25, 200))
            screen.blit(t, (100, 180))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
    
    def LOSE():
        screen.fill((0, 0, 0))
        time.sleep(0.5)
        screen.blit(text2, (100, 180))
        pygame.display.update()
        time.sleep(1)
        
    if snake.lose:
        d = 5
        level1 = False
        level2 = False
        level3 = False
        screen.fill((0, 0, 0))
        snake.size = 1
        snake.elements.clear()
        snake.elements = [[200, 100]]
        SCORE1 = 0
        snake.dx = d
        snake.dy = 0
        pygame.draw.rect(screen, (220, 10, 60), (100, 60, 200, 50))
        pygame.draw.rect(screen, (220, 10, 60), (100, 140, 200, 50))
        pygame.draw.rect(screen, (220, 10, 60), (100, 220, 200, 50))
        pygame.draw.rect(screen, (60, 10, 220), (100, 300, 200, 50))
        screen.blit(t1, (159, 70))
        screen.blit(t2, (135, 150))
        screen.blit(t3, (160, 230))
        screen.blit(t4, (125, 310))
        snake.lose = False

    pygame.display.flip()

pygame.quit()