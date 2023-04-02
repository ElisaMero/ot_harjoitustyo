#muista git push yms..!
#import unittest ??!

import pygame
import os

dirname = os.path.dirname(__file__)

class PlatformJumpingGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((840,780))
        self.loop()

    def loop(self):
        while True:
            self.background()
            self.graphics()
            self.events()
        
    def background(self):
        pygame.display.set_caption("Jumping Game")
        self.screen.fill((173, 255, 255))
        pygame.draw.circle(self.screen, (255,255,255), (100, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (150, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 85), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 100), 20)

    
    def graphics(self):
        
        #tähän importtaa playerimage.py!

        pygame.display.flip()

    def events(self):
        player = pygame.image.load(
            os.path.join(dirname, "images", "box.png")
        )
        x = 55-player.get_width()
        y = 700-player.get_height()

        right = False
        left = False
        up = False
        down = False

        clock = pygame.time.Clock()

        while True:
            for happens in pygame.event.get():
                if happens.type == pygame.KEYDOWN:
                    #ei saavuta
                    key = happens.key
                    if key == pygame.K_LEFT:
                        left = True
                    if happens.key == pygame.K_RIGHT:
                        exit()
                        right = True

                # onko välttämättömiä hyppäämisen kannalta?:
                    if key == pygame.K_UP:
                        up = True
                    if key == pygame.K_DOWN:
                        down = True
              
                #self.variables = (x,y)

                if happens.type == pygame.KEYUP:
                    key = happens.key
                    if key == pygame.K_LEFT:
                        left = False
                    if key == pygame.K_RIGHT:
                        right = False
                    if key == pygame.K_UP:
                        up = False
                    if key == pygame.K_DOWN:
                        down = False

        
                if happens.type == pygame.QUIT:
                    exit()
                

            if right:
                x += 15
            if left:
                x -= 15
            if up:
                y += 15
            if down:
                y -= 15
            
            self.graphics()
            self.screen.blit(player, (x,y))
            pygame.display.flip()
 

            clock.tick(60)

            while True:
                for tapahtuma in pygame.event.get():
                    if tapahtuma.type == pygame.QUIT:
                        exit()
  


if __name__== "__main__":
    PlatformJumpingGame()





