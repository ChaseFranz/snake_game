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
        self.snake = Snake(self.surface,self.size,6)
        self.snake.draw()
        self.apple = Apple(self.surface,self.size)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

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