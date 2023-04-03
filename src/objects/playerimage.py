
import pygame
import os


dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    def __init__(self, x=50, y=400):

        super().__init__()

        self.player = pygame.image.load(
            os.path.join(dirname, "..", "images", "box.png")
        )

        self.rect = self.player.get_rect()

        self.rect.x = x
        self.rect.y = y

    def letters(self, h):
        if h == "x":
            return self.rect.x
        if h == "y":
            return self.rect.y

    def events(self, direction):


        if direction == "right":
            self.rect.x += 15
        if direction == "left":
            self.rect.x -= 15
        if direction == "up":
           self.rect.y += 15
        if direction == "down":
            self.rect.y -= 15
        if direction == "stop":
            self.rect.y == 0
            self.rect.x == 0
            


                

                




