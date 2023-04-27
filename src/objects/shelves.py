import pygame


class Shelves(pygame.sprite.Sprite):
    """Luokka, joka vastaa hyppäystasojen piirtämisestä
    halutun kokoiseksi ja haluttuun kohtaan

    Attribuutit:
        self.image = määrittelee koon pinnalle
        .fill antaa pinnalle värin
        self.rect = tarvitaan spritecolliden toiminnassa
        self.rect.x = x-koordinaatti
        self.rect.y = y-koordinaatti
    """
    def __init__(self, x_koord, y_koord, width, height):
        """    Args:
        self.image = määrittelee koon pinnalle
        .fill antaa pinnalle värin
        self.rect = tarvitaan spritecolliden toiminnassa
        self.rect.x = x-koordinaatti
        self.rect.y = y-koordinaatti
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((246, 202, 161))
        self.rect = self.image.get_rect()
        self.rect.x = x_koord
        self.rect.y = y_koord
