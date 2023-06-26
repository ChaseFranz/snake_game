import pygame
import random

class Apple:
    def __init__(self, parent_screen, size):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.size = size
        self.parent_screen = parent_screen
        self.x = self.size*3
        self.y = self.size*3
    
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.x = random.randint(0,24)*self.size
        self.y = random.randint(0,19)*self.size