
import os
import pygame
from stop import StopScreen
VectorMoving = pygame.math.Vector2

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, mainplatform):
        super().__init__()

        self.mainplatform = mainplatform
        self.stop = StopScreen()

        self.user = pygame.image.load(
            os.path.join(dirname, "..", "images", "box.png")
        )

        self.rect = self.user.get_rect()

        self.rect.center = (40, 690)
        self.position = VectorMoving(40, 690)
        self.velocity = VectorMoving(0, 0)
        self.acceleration = VectorMoving(0, 0.0)

    def gravity(self):
        self.acceleration = VectorMoving(0, 0.51)
        pygame.display.update()

    def events(self, direction):
        if direction == "right":
            self.acceleration.x += 0.2
        if direction == "left":
            self.acceleration.x -= 0.2

        if direction == "jump":
            self.rect.x += 1
            collision = pygame.sprite.spritecollide(
                self, self.mainplatform.shelves, False)
            self.rect.x -= 1
            if collision:
                self.velocity.y = -15
                collision = False
        self.events2()

    def events2(self):

        # physics equations for moving:
        self.acceleration.x += self.velocity.x * -0.007
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if self.position.x > 840:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = 840

        self.rect.midbottom = self.position

        if self.position.y > 800:
            self.stop.last_loop()
