#muista git push yms..!
#import unittest ??!

import os
import pygame
from objects.playerimage import Player

dirname = os.path.dirname(__file__)

class PlatformJumpingGame:
    def __init__(self):
        pygame.init()

        self.player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.screen = pygame.display.set_mode((840,780))

        self.loop()


    def loop(self):
        while True:
            self.background()
            self.moving()
            self.all_sprites.draw(self.screen)
            
            
        
    def background(self):
        pygame.display.set_caption("Jumping Game")
        self.screen.fill((173, 255, 255))
        pygame.draw.circle(self.screen, (255,255,255), (100, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (150, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 85), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 100), 20)
        
  

    def moving(self):
        clock = pygame.time.Clock()

       
        while True:
            for happens in pygame.event.get():
                if happens.type == pygame.QUIT:
                    exit()
                if happens.type == pygame.KEYDOWN:
                    key = happens.key
                    if key == pygame.K_LEFT:
                        self.player.events("left")
                    if happens.key == pygame.K_RIGHT:
                    
                        self.player.events("right")
                    if key == pygame.K_UP:
                        
                        self.player.events("up")
                    if key == pygame.K_DOWN:
                        self.player.events("down")

                

                if happens.type == pygame.KEYUP:
                    key = happens.key
                    self.player.events("stop")

                        
            pygame.display.flip()
            clock.tick(60)



if __name__== "__main__":
    PlatformJumpingGame()





