#muista git push yms..!
#import unittest?!
#import os??

import pygame
#from controls import Movements

class PlatformJumpingGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((840,780))
        self.screen.fill((173, 255, 255))
        self.x = 50
        self.y = 750
        self.player = pygame.draw.circle(self.screen, "blue", (self.x, self.y), 20)

        pygame.draw.circle(self.screen, (255,255,255), (100, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (150, 100), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 85), 20)
        pygame.draw.circle(self.screen, (255,255,255), (125, 100), 20)

        self.loop()

    def loop(self):
        self.screenview()
        self.item1()
        
    def background(self):
        pass
        
    
    def screenview(self):
        pygame.display.set_caption("Jumping Game")
        pygame.display.flip()
        self.item1()
        while True:
            for happening in pygame.event.get():
                if happening.type == pygame.QUIT:
                    exit()
        
    def drawing(self, coordinates):
            pygame.display.update()
            self.player = pygame.draw.circle(self.screen, "blue", (coordinates), 20)

            #self.screen.blit(player, (x,y)) wut

            pygame.display.update()
            self.item1()

    
    def item1(self):
        #Movements.draw() misk eitoimi importtaaminen, selvitä!
        #alustava kokeilu pallon hallinnasta ja luonnista:


        clock = pygame.time.Clock()
        pygame.display.update()

        coordinates = (self.x, self.y)

        left = False
        right = False
        up = False
        down = False



        while True:
            for happens in pygame.event.get():
                if happens.type == pygame.KEYDOWN:
                    key = happens.key
                    if key == pygame.K_LEFT:
                        left = True
                        self.x -= 10
                        self.drawing(coordinates)
                    if key == pygame.K_RIGHT:
                        right = True
                        self.x += 10
                        self.drawing(coordinates)


                # onko välttämättömiä hyppäämisen kannalta?:
                    if key == pygame.K_UP:
                        up = True
                        self.y -= 10
                        self.drawing(coordinates)
                    if key == pygame.K_DOWN:
                        down = True
                        self.y += 10
                        self.drawing(coordinates)
        
                if happens.type == pygame.QUIT:
                    exit()
                

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
                
 

            pygame.display.update()
            pygame.display.flip()
            clock.tick(60)
  


if __name__== "__main__":
    PlatformJumpingGame()





