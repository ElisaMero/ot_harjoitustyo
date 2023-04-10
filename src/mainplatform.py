#muista git push yms..!
#import unittest ??!

import os
import pygame
from objects.playerimage import Player

dirname = os.path.dirname(__file__)

class PlatformJumpingGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((840,780))

        self.player = Player()

        self.loop()


    def loop(self):
        while True:
            self.background()
            self.moving()
            
            
        
    def background(self):
        pygame.display.set_caption("Jumping Game")
        self.screen.fill((173, 255, 255))
        pygame.draw.circle(self.screen, (255,255,255), (100, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (150, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 85), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 100), 20)
        self.draw_player()


    def draw_player(self):
        self.player.all_sprites.draw(self.screen)
        self.screen.blit(self.player.user, (self.player.rect.x, self.player.rect.y))
        pygame.display.update() 
  

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
                        self.draw_player()
                    if happens.key == pygame.K_RIGHT:
                        self.player.events("right")
                        self.draw_player()
                    if key == pygame.K_UP:
                        self.player.events("up")
                        self.draw_player()
                    if key == pygame.K_DOWN:
                        self.player.events("down")
                        self.draw_player()

                

                if happens.type == pygame.KEYUP:
                    key = happens.key
                    self.player.events("stop")
     
            pygame.display.update()    
            pygame.display.flip()
            clock.tick(60)



if __name__== "__main__":
    PlatformJumpingGame()



