import pygame
import time
from pygame.locals import *

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3
    
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        # init screen and block
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()

        # init block location
        self.x = [SIZE] * length
        self.y = [SIZE] * length

        # direction constants
        self.up = 'up'
        self.down = 'down'
        self.left = 'left'
        self.right = 'right'

        # init direction
        self.direction = self.down

    # fill screen, draw block, refresh screen
    def draw(self):
        self.parent_screen.fill((110,110,5))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = self.left

    def move_right(self):
        self.direction = self.right

    def move_down(self):
        self.direction = self.down

    def move_up(self):
        self.direction = self.up

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == self.up:
            self.y[0] -= SIZE
        if self.direction == self.down:
            self.y[0] += SIZE
        if self.direction == self.left:
            self.x[0] -= SIZE
        if self.direction == self.right:
            self.x[0] += SIZE
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface,6)
        self.snake.draw()
        self.apple = Apple(self.surface)
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

# MAIN MODULE          
if __name__ == "__main__":
    game = Game()
    game.run()