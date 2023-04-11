
import pygame
import os


dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.user = pygame.image.load(
            os.path.join(dirname, "..", "images", "box.png")
        )

        self.rect = self.user.get_rect()

        self.rect.x = 40
        self.rect.y = 690
        self.all_sprites = pygame.sprite.Group()
        self.jump_velocity = 20

    def sprite(self):
        self.all_sprites.add(self.user)


    def events(self, direction):

        if direction == "right" and self.rect.x < 800:
            self.rect.x += 8
        if direction == "left" and self.rect.x > 0:
            self.rect.x -= 8

        if direction == "jump":
            self.rect.y -= self.jump_velocity
            self.jump_velocity -= 2
            if self.jump_velocity < -20:
                self.jump_velocity = 20

        

 




            



                

                




