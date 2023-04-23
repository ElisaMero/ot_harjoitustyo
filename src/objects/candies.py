
import pygame


class Candies(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, width):
        super().__init__()

        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (249, 194, 240),
                           (radius, radius), radius, width)
        self.rect = self.image.get_rect(center=(x, y))
