
import pygame

#from mainplatform import PlatformJumpingGame 



class Surfaces(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.rect.x2 = 590
        self.rect.y2 = 650


        #self.main = PlatformJumpingGame()

        #self.rect = self.surface.get_rect()

        self.all_sprites = pygame.sprite.Group()


    def sprite(self):
        self.all_sprites.add(self.surface)

    def draw_surfaces(self):
        self.all_sprites = pygame.sprite.Group()
        self.surface = pygame.draw.rect(self.screen, (246,202,161), (590, 650, 130, 20))
        self.all_sprites.add(self.surface)
        self.surface = pygame.sprite.Group()
        collisions = pygame.sprite.spritecollide(self.player.player, self.surface, False)
        if collisions:
            self.player.rect.y = collisions[0].rect.top
            self.jumping = False
       