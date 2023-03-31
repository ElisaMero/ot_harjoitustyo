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

    #testausvaiheessa, siirrettävä omaan tiedostoon
        pygame.draw.circle(self.screen, "blue", (90,650), 20)
        pygame.display.flip()


if __name__== "__main__":
    PlatformJumpingGame()






