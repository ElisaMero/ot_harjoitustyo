
import sys
import pygame

class StopScreen:
    """Luokka, joka vastaa lopetusnäytöstä
    Attribuutit:
        self.screen3 = piirtää näytön ja asettaa sille koon.
    """

    def __init__(self):
        """Args:
        self.screen3 = piirtää näytön ja asettaa sille koon.
        """
        self.screen3 = pygame.display.set_mode((840, 780))

    def last_loop(self):
        """Vastaa näytön piirtofunktion kutsumisesta.
        """
        self.last_graphics()
        self.stop_game()

    def last_graphics(self):
        """Vastaa lopetusnäytön piirtämisestä.
        """
        pygame.display.set_caption("Jumping Game")
        self.screen3.fill((173, 255, 255))
        pygame.draw.circle(self.screen3, (255, 255, 255), (100, 100), 20)
        pygame.draw.circle(self.screen3, (255, 255, 255), (150, 100), 20)
        pygame.draw.circle(self.screen3, (255, 255, 255), (125, 85), 20)
        pygame.draw.circle(self.screen3, (255, 255, 255), (125, 100), 20)

        pygame.draw.rect(self.screen3, (249, 194, 240),
                         (170, 340, 480, 210))
        font = pygame.font.SysFont("Arial", 85)
        text = font.render("Game Over", True, (255, 255, 255))
        self.screen3.blit(text, (190, 380))
        pygame.display.flip()

    def stop_game(self):
        """Vastaa toiminnoista.
        Raksia painamalla voi sulkea pelin.
        """
        clock = pygame.time.Clock()
        run = True
        while run:
            pygame.display.update()
            for happens in pygame.event.get():
                if happens.type == pygame.QUIT:
                    run = False
                    sys.exit()

                clock.tick(60)
