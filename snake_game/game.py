import pygame
import time
from pygame.locals import *
from apple import *
from snake import *

class Game:
    def __init__(self):
        pygame.init()
        self.size = 40
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface,self.size,1)
        self.snake.draw()
        self.apple = Apple(self.surface,self.size)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}", True, (255,255,255))
        self.surface.blit(score,(800,10))

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + self.size:
            if y1 >= y2 and y1 < y2 + self.size:
                return True
        
    def play(self):
        self.surface.fill((110,110,5))
        self.apple.draw()
        self.snake.walk()
        self.display_score()
        pygame.display.flip()

        # Check if collision with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # Check if collision with self
        for i in range(1,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print("game over")
                exit(0)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.3)