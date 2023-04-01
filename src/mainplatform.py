#muista git push yms..!
#import unittest?!
#import os??


import pygame

class PlatformJumpingGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((840,780))
        self.screen.fill((173, 255, 255))

        self.loop()

    def loop(self):
        self.screenview()
        self.item1()
        
    
    def screenview(self):
        pygame.display.set_caption("Jumping Game")
        pygame.display.flip()
        self.item1()
        while True:
            for happening in pygame.event.get():
                if happening.type == pygame.QUIT:
                    exit()
        
    def item1(self):

      #alustava kokeilu pallon hallinnasta ja luonnista:

        x = 90
        y = 650
 
        

        

        oikealle = False
        vasemmalle = False
        ylos = False
        alas = False
        clock = pygame.time.Clock()
        
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_LEFT:
                        vasemmalle = True
                    if tapahtuma.key == pygame.K_RIGHT:
                        oikealle = True
                    if tapahtuma.key == pygame.K_UP:
                        ylos = True
                    if tapahtuma.key == pygame.K_DOWN:
                        alas = True
                # huomaa ero: K_UP ja pygame.KEYUP !!
        
                if tapahtuma.type == pygame.KEYUP:
                    if tapahtuma.key == pygame.K_LEFT:
                        vasemmalle = False
                    if tapahtuma.key == pygame.K_RIGHT:
                        oikealle = False
                    if tapahtuma.key == pygame.K_UP:
                        ylos = False
                    if tapahtuma.key == pygame.K_DOWN:
                        alas = False
        
                if tapahtuma.type == pygame.QUIT:
                    exit()
 
            if oikealle:
                x += 2
            if vasemmalle:
                x -= 2
            if ylos:
                y -= 2
            if alas:
                y += 2

            player = pygame.draw.circle(self.screen, "blue", (x, y), 20)


            #self.screen.blit(player, (x,y)) wut

            pygame.display.update()


            
            pygame.display.flip()
            clock.tick(60)
           





  
  


if __name__== "__main__":
    PlatformJumpingGame()






