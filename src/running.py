
import pygame
from mainplatform import PlatformJumpingGame
from start import StartScreen


class GameLoop:
    def __init__(self):
        pygame.init()
        self.start = StartScreen()
        self.main = PlatformJumpingGame()

        self.gameloop()

    def gameloop(self):
        self.start.startloop()

        self.main.sprite_add_player()


if __name__ == "__main__":
    GameLoop()
