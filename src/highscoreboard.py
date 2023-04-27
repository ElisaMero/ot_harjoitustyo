
import sys
import pygame
from repositories.database import SaveData


class Board:
    """Luokka, joka vastaa tulostaulunäkymästä.
    Attribuutit:
        self.screen4 = avaa näytön ja asettaa sille koon.
        self.data = yhdistää SaveData-luokan Board-luokkaan.
    """
    def __init__(self):
        """
        Args:
        self.screen4 = avaa näytön ja asettaa sille koon.
        self.data = yhdistää SaveData-luokan Board-luokkaan.
        """
        self.screen4 = pygame.display.set_mode((840, 780))
        self.data = SaveData(None)

    def board_loop(self):
        """Silmukka, joka pyörittää näkymää
        Kutsuu piirtofunktiota
        """
        while True:
            self.board_graphics()
            break

    def board_graphics(self):
        """Piirtää käyttäjälle näkymän taulusta
        Kutsuu funktiota, joka vastaa tuloksista.
        """
        pygame.display.set_caption("Jumping Game")
        self.screen4.fill((173, 255, 255))
        pygame.draw.circle(self.screen4, (255, 255, 255), (100, 100), 20)
        pygame.draw.circle(self.screen4, (255, 255, 255), (150, 100), 20)
        pygame.draw.circle(self.screen4, (255, 255, 255), (125, 85), 20)
        pygame.draw.circle(self.screen4, (255, 255, 255), (125, 100), 20)

        font = pygame.font.SysFont("Arial", 90)
        text = font.render("Highscores", True, (255, 255, 255))
        self.screen4.blit(text, (70, 130))
        font2 = pygame.font.SysFont("Arial", 40)
        text2 = font2.render("Press ENTER to start game",
                             True, (255, 255, 255))
        self.screen4.blit(text2, (70, 680))

        pygame.display.flip()
        pygame.display.update()
        self.get_scores_on_screen()

    def get_scores_on_screen(self):
        """Vastaa listan hausta SaveData-luokasta,
        ja näyttää sisällön käyttäjälle. 
        datalistille on annettu arvoksi lista viidestä
        parhaasta tuloksesta, joka piirretään
        näytölle järjestyksessä. 
        """
        datalist = self.data.scores_in_order()
        order = 1
        y_koordinate = 290
        font3 = pygame.font.SysFont("Arial", 40)
        for j in datalist:
            text3 = font3.render(f"{order}. {j}", True, (255, 255, 255))
            self.screen4.blit(text3, (70, y_koordinate))
            order += 1
            y_koordinate += 70
        pygame.display.flip()
        pygame.display.update()

        self.board_events()

    def board_events(self):
        """Vastaa luokan tapahtumista. Raksia painamalla
        näyttö sulkeutuu.
        Näppäimistön painiketta painamalla pääsee pelinäkymään.
        """
        clock = pygame.time.Clock()

        for happens in pygame.event.get():
            if happens.type == pygame.QUIT:
                sys.exit()

            if happens.type == pygame.KEYDOWN:
                return

            clock.tick(60)
