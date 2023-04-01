import pygame
from mainplatform import PlatformJumpingGame
#from elements import pygamepictures (?)

class Movements:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.draw.circle(self.screen, "blue", (100, 100), 20)
        self.draw()

    def draw():
        pygame.draw.circle(PlatformJumpingGame.self.screen, "blue", (100, 100), 20)

if __name__ == "__main__":
    Movements()