import pygame


class Shelves(pygame.sprite.Sprite):
    """Luokka, joka vastaa hyppäystasojen 

    Args:
        pygame (_type_): _description_
    """
    def __init__(self, x_koord, y_koord, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((246, 202, 161))
        self.rect = self.image.get_rect()
        self.rect.x = x_koord
        self.rect.y = y_koord
