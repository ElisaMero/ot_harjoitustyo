
import sys
import pygame
from highscoreboard import Board


class StartScreen:
    """Luokka, joka on vastuussa aloitusnäytöstä
    Attribuutit:
        self.screen2 = pygamen näytön piirtäminen 
        self.board = yhdistetään tulostaulu luokkaan Board, 
        jotta kyseisen luokan funktiota voidaan kutsua. 
    """

    def __init__(self):
        """ Args:
        self.screen2 = pygamen näytön piirtäminen 
        self.board = yhdistetään tulostaulu luokkaan Board, 
        jotta kyseisen luokan funktiota voidaan kutsua. 
        """
        self.screen2 = pygame.display.set_mode((840, 780))
        self.board = Board()

    def startloop(self):
        """Kutsuu luokan funktioita
        """
        self.graphics2()
        self.startgame()

    def graphics2(self):
        """Asettaa nimen pelille ja piirtää grafiikat
        """
        pygame.display.set_caption("Jumping Game")
        self.screen2.fill((173, 255, 255))
        pygame.draw.circle(self.screen2, (255, 255, 255), (100, 100), 20)
        pygame.draw.circle(self.screen2, (255, 255, 255), (150, 100), 20)
        pygame.draw.circle(self.screen2, (255, 255, 255), (125, 85), 20)
        pygame.draw.circle(self.screen2, (255, 255, 255), (125, 100), 20)

        pygame.draw.rect(self.screen2, (249, 194, 240),
                         (220, 340, 430, 210))
        font = pygame.font.SysFont("Arial", 90)
        font2 = pygame.font.SysFont("Arial", 50)
        text = font.render("Start", True, (255, 255, 255))
        text2 = font2.render("Press 2 to start", True, (255, 255, 255))
        self.screen2.blit(text, (310, 380))
        self.screen2.blit(text2, (70, 180))

        font3 = pygame.font.SysFont("Arial", 50)
        text3 = font3.render("Press 1 to see highscores",
                             True, (255, 255, 255))
        self.screen2.blit(text3, (70, 610))
        pygame.display.flip()

    def startgame(self):
        """Vastaa tapahtumista.
        Jos halutaan sulkea peli rastista, se onnistuu.
        Jos näppäimistöltä painetaan 1, 
        kutsutaan Board-luokan funktiota, 
        jolloin käyttäjälle näkyy tulostaulu.
        Painamalla 2, saa pelin avattua suoraan.
        """
        while True:
            for happens in pygame.event.get():
                if happens.type == pygame.QUIT:
                    sys.exit()

            usercontrol = pygame.key.get_pressed()
            if usercontrol[pygame.K_1]:
                self.board.board_loop()
            if usercontrol[pygame.K_2]:
                return
