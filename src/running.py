
import pygame
from mainplatform import PlatformJumpingGame
from start import StartScreen


class GameLoop:
    """Luokka, joka vastaa koko pelin pyörittämisestä.
    Attribuutit:
        self.start = yhdistää tähän luokkaan aloitusnäyttöluokan StartScreenin
        self.main = yhdistää tähän luokkaan myös luokan, joka on vastuussa pelin 
        piirtämisestä ja päivityksestä.
    """

    def __init__(self):
        """    Args:
        self.start = yhdistää tähän luokkaan aloitusnäyttöluokan StartScreenin
        self.main = yhdistää tähän luokkaan myös luokan, joka on vastuussa pelin 
        piirtämisestä ja päivityksestä.
        Kutsutaan gamelooppia, joka aloittaa pelin pyörituksen alkunäkymästä.
        """
        pygame.init()
        self.start = StartScreen()
        self.main = PlatformJumpingGame()
        self.gameloop()

    def gameloop(self):
        """Aloittaa pelin pyörityksen alkunäkymästä asti, jonka jälkeen aloitetaan itse peli 
        kutsumalla pelin piirtoluokkaa. 
        """
        self.start.startloop()
        self.main.add_sprites()
        


if __name__ == "__main__":
    GameLoop()
