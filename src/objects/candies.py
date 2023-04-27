
import pygame


class Candies(pygame.sprite.Sprite):
    """Luokka, joka vastaa karkin piirrosta 
    halutun kokoiseksi ja paikkaan, joka arvotaan
    satunnaisesti. 

    Attribuutit:
        self.image = määrittelee koon pinnalle
        pygame.draw.circle piirtää kuvan annettujen
        parametrien avulla.
        self.rect =  objektin ulottuvuukseien määrittely
    """

    def __init__(self, x_koord, y_koord, radius, width):
        """
        Args:
        self.image = määrittelee koon pinnalle
        pygame.draw.circle piirtää kuvan annettujen
        parametrien avulla.
        self.rect =  objektin ulottuvuukseien määrittely
        """
        super().__init__()

        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (249, 194, 240),
                           (radius, radius), radius, width)
        self.rect = self.image.get_rect(center=(x_koord, y_koord))
