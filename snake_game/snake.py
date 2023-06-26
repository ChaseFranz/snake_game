import pygame

class Snake:
    def __init__(self, parent_screen, size, length):
        self.length = length
        self.size = size
        # init screen and block
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()

        # init block location
        self.x = [self.size] * length
        self.y = [self.size] * length

        # direction constants
        self.up = 'up'
        self.down = 'down'
        self.left = 'left'
        self.right = 'right'

        # init direction
        self.direction = self.down

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    # fill screen, draw block, refresh screen
    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))

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
            self.y[0] -= self.size
        if self.direction == self.down:
            self.y[0] += self.size
        if self.direction == self.left:
            self.x[0] -= self.size
        if self.direction == self.right:
            self.x[0] += self.size
        self.draw()