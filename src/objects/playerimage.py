
import os
import pygame
vector = pygame.math.Vector2

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, mp):
        super().__init__()

        self.mp = mp

        self.user = pygame.image.load(
            os.path.join(dirname, "..", "images", "box.png")
        )

        self.rect = self.user.get_rect()

        self.rect.center = (40, 690)
        self.position = vector(40, 690)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0.7)

    def gravity(self):
        self.acceleration = vector(0, 0.5)
        pygame.display.update()

    def events(self, direction):
        self.acceleration = vector(0, 0.5)
        if direction == "right":
            self.acceleration.x += 0.2
        if direction == "left":
            self.acceleration.x -= 0.2

        if direction == "jump":
            self.rect.x += 1
            collision = pygame.sprite.spritecollide(
                self, self.mp.shelves, False)
            self.rect.x -= 1
            if collision:
                self.velocity.y = -15
                collision = False
                
        # physics equations for moving:
        self.acceleration.x += self.velocity.x * -0.01
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if self.position.x > 840:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = 840

        self.rect.midbottom = self.position
