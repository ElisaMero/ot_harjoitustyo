
import pygame
import os


dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        self.user = pygame.image.load(
            os.path.join(dirname, "..", "images", "box.png")
        )

        #surface?, also pitääks määrittää et
        #  tää piirretää self.screenille ??


        self.rect = self.user.get_rect()

        self.rect.x = 50
        self.rect.y = 550
        self.all_sprites = pygame.sprite.Group()

    def sprite(self):
        self.all_sprites.add(self.user)

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
           self.rect.y -= 15
        if direction == "down":
            self.rect.y += 15
        if direction == "stop":
            self.rect.y == 0
            self.rect.x == 0
 




            



                

                




