import pygame
import time
from pygame.locals import *
from apple import *
from snake import *

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.size = 40
        self.background_color = (110,110,5)
        self.font_color = (255,255,255)
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill(self.background_color)
        self.snake = Snake(self.surface,self.size,1)
        self.snake.draw()
        self.apple = Apple(self.surface,self.size)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}", True, self.font_color)
        self.surface.blit(score,(800,10))

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + self.size:
            if y1 >= y2 and y1 < y2 + self.size:
                return True
        
    def play(self):
        self.surface.fill(self.background_color)
        self.apple.draw()
        self.snake.walk()
        self.display_score()
        pygame.display.update()

        # Check if collision with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # Check if collision with self
        for i in range(1,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"

    def reset(self):
        self.snake = Snake(self.surface, self.size, 1)
        self.apple = Apple(self.surface, self.size)

    def run(self):
        running = True
        pause = False
        FPS = 60
        
        while running:
            # Handle user input
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                    if event.key == K_RETURN:
                        pause = False
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

            # Try to run game logic
            try:
                if not pause:
                    self.play()
            except Exception as e:
                pause = True
                self.show_game_over()
                self.reset()

            self.clock.tick(6)
    
    def show_game_over(self):
        self.surface.fill(self.background_color)
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"Game is over! Your score is: {self.snake.length}", True, self.font_color)
        self.surface.blit(line1,(200,200))
        line2 = font.render("To play again press Enter. To exit press Escape:", True, self.font_color)
        self.surface.blit(line2,(200,350))
        pygame.display.flip()