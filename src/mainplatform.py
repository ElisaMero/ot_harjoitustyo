
import sys
from random import randint
import pygame
from objects.playerimage import Player
from objects.shelves import Shelves
from objects.candies import Candies
from repositories.database import SaveData
from stop import StopScreen


class PlatformJumpingGame():
    """Luokka, joka on vastuussa grafiikoiden ja tapahtumien päivityksestä.
    Kaikki funktiot, jotka tarvitsevat self.screen-muuttujaa
    toimiakseen.
    Attribuutit: 
        self.screen = näyttö ja sen korkeus
        self.player = player joka saa itselleen kopion tästä luokasta
        self.jumping = katsoo, onko pelaaja tasolla vai ilmassa, 
        alussa epätosi booleanin arvo
        self.calculator = laskee osumat karkkien kohdalla, alkaa 0:sta
        all_sprites ja shelves ovat sprite.Grouppeja, 
        joiden avulla spritecollide-toiminto on mahdollista
        self.clock = pygamen kello
     """

    def __init__(self):
        """    Args: 
        self.screen = näyttö ja sen korkeus
        self.player = player joka saa itselleen kopion tästä luokasta
        self.jumping = asettaa pelaajan hyppimisen päälle 
        self.calculator = laskee osumat karkkien kohdalla, alkaa 0:sta
        self.clock = pygamen kello
        """
        self.screen = pygame.display.set_mode((840, 780))
        self.player = Player(self)
        self.stop = StopScreen()
        self.jumping = True
        self.all_sprites = pygame.sprite.Group()
        self.shelves = pygame.sprite.Group()
        self.calculator = 0

    def loop(self):
        """Pelin silmukka, joka pyörittää peliä
        """
        while True:
            self.backrounds()
            self.draw_all()
            self.player.gravity()
            self.candy_collision()
            self.score()
            self.moving()

    def backrounds(self):
        """Silmukka, joka kutsuu funktiot, joiden avulla piirretään
        pelin taustagrafiikat sekä seuraavaa pelisilmukkaa. 
        """
        self.background()
        self.more_backround()
        self.new_loop()

    def background(self):
        """_Annetaan pelille nimi ja asetetaan näytön väri, ja piirretään pilvikuvioita
        """
        pygame.display.update()
        pygame.display.set_caption("Jumping Game")
        self.screen.fill((173, 255, 255))
        pygame.draw.circle(self.screen, (255, 255, 255), (100, 100), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (150, 100), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (125, 85), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (125, 100), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (350, 150), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (400, 150), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (375, 135), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (375, 150), 20)
        self.more_backround()

    def more_backround(self):
        """Piirretään vaaran kyltti näytölle.
        Alla on lisää pelisilmukoita, sillä pelin toiminta vaatii uudelleenkutsumisen.
        """
        pygame.draw.rect(self.screen, (149, 113, 85), (375, 710, 73, 33))
        pygame.draw.rect(self.screen, (149, 113, 85), (400, 715, 10, 60))
        font = pygame.font.SysFont("Arial", 20)
        text1 = font.render("Danger!", True, (255, 255, 255))
        self.screen.blit(text1, (376, 715))
        self.new_loop()

    def new_loop(self):
        """Silmukka, joka kutsuu funktioita, joiden avulla päivitetään
        pelaajaobjektin koordinaatit sekä tarkastetaan, tapahtuiko
        pelaajan ja karkin välillä osumaa.
        """
        self.player.gravity()
        self.candy_collision()
        self.draw_all()
        self.score()

    def sprite_add_player(self):
        """Lisätään pelaaja yhteiseen sprite.Grouppiin
        """
        self.all_sprites.add(self.player)

    def add_sprites(self):
        """Lisätään pelin hyppytasot, pelaaja sekä kerättävä karkki omiin ja yhteisiin 
        sprite.Grouppeihin mahdollistaakseen spritecolliden toiminnan.
        """
        self.sprite_add_player()
        self.make_surfaces()
        self.draw_candy()
        self.loop()

    def make_surfaces(self):
        """Piirretään laudat omille paikoilleen Shelves-classin avulla. 
        Shelf3 ja shel5 ovat pelin "lattian" osat.
        """
        shelf1 = Shelves(560, 620, 130, 20)
        shelf2 = Shelves(100, 200, 130, 20)
        shelf3 = Shelves(0, 760, 295, 20)   
        shelf4 = Shelves(530, 370, 130, 20)
        shelf5 = Shelves(390, 760, 485, 20)  
        shelf6 = Shelves(100, 490, 130, 20)
        shelf7 = Shelves(400, 270, 130, 20)
        shelvelist = [shelf1, shelf2, shelf3, shelf4, shelf5, shelf6, shelf7]

        self.add_in_all_sprites(shelvelist)
        self.add_in_shelves(shelvelist)

    def add_in_all_sprites(self, shelvelist):
        """Lisätään osa laudoista kaikkien sprite.Grouppiin
        """
        for i in shelvelist:
            self.all_sprites.add(i)

    def add_in_shelves(self, shelvelist):
        """Lisätään laudat omaan sprite.Grouppiin
        """
        for i in shelvelist:
            self.shelves.add(i)

    def draw_candy(self):
        """Piirretään karkki oman Candies-luokan avulla ja syötetään satunnaiset koordinaatit.
        Luodaan karkille oma sprite.Group, sillä se on välttämätön spritecolliden toiminnan kannalta
        Koska koodi luo uuden karkin joka osuman jälkeen, joudumme luoda sprite.Groupin uudelleen
        Lisätään karkki myös kaikkien yhteiseen sprite.Grouppiin.
        """
        self.candysprite = pygame.sprite.Group()
        candy_in_screen = Candies(randint(15, 600), randint(15, 630), 15, 20)
        self.all_sprites.add(candy_in_screen)
        self.candysprite.add(candy_in_screen)

    def draw_all(self):
        """Piirretään kaikki näytölle.
        """
        self.player.gravity()
        self.shelves.draw(self.screen)
        self.candysprite.draw(self.screen)
        self.screen.blit(self.player.user, (self.player.rect.center))
        self.all_sprites.update()
        pygame.display.update()
        pygame.display.flip()

    def candy_collision(self):
        """Tarkastellaan osumia pelaajan ja karkin välillä.
        Osuman sattuessa collision2 muutetaan todeksi
        ja kutsutaan laskurifuntiota kirjaamaan osuma.
        """
        collision2 = pygame.sprite.spritecollide(
            self.player, self.candysprite, False)
        if collision2:
            self.player.position.y = collision2[0].rect.top
            self.counter()
        else:
            pass

    def counter(self):
        """Kutsuu laskurifunktiota kirjaamaan osuman, päivittää osuman näytölle sekä
        kutsuu karkin piirtofunktiota uuden karkin luomista varten.
        """
        self.calculator1()
        self.score()
        self.draw_candy()

    def calculator1(self):
        """Kirjaa osuman laskuriin
        """
        self.calculator += 1

    def score(self):
        """Päivittää osuman määrän näytölle
        """
        font = pygame.font.SysFont("Arial", 40)
        text = font.render(f"Score: {self.calculator}", True, (255, 255, 255))
        self.screen.blit(text, (630, 80))
        pygame.display.flip()

    def end_game(self):
        """Vastaa pelin tuloksen talteen ottamisesta antamalla se SaveData-luokalle.
        Tämän jälkeen kutsutaan lopetusnäytön aloitusfunktiota.
        """
        SaveData(self.calculator)
        self.stop.last_loop()

    def moving(self):
        """On vastuussa näppäimistöstä ja pygamen raksipainikkeen toiminnasta.
        Oikean nuolinäppäimen painallus kutsuu Player-luokan events-funktiota, antamalla samalla 
        sille arvon "right". Vasenta luolinäppäintä painaessa samalle funkiolle "left"-arvo.
        "Events-funktiolle syötetään toistuvasti "jump"-käsky, joka pitää pelaajan hyppimässä.
        Kyseisen events-funktion suorituksen jälkeen päivitetään x ja y koordinaattien 
        muutokset näytölle kutsumalla piirtofunktiota.
        Päivitetään muutokset kutsumalla update-funktiota.
        """
        self.draw_all()
        clock = pygame.time.Clock()
        while True:
            self.background()
            for happens in pygame.event.get():
                if happens.type == pygame.QUIT:
                    sys.exit()
            usercontrol = pygame.key.get_pressed()
            if usercontrol[pygame.K_RIGHT]:
                self.player.events("right")
                self.draw_all()
            if usercontrol[pygame.K_LEFT]:
                self.player.events("left")
                self.draw_all()
            if self.jumping:
                self.player.events("jump")
                if self.player.velocity.y == 15:
                    self.make_surfaces()
            clock.tick(60)
            pygame.display.flip()
            pygame.time.delay(20)
