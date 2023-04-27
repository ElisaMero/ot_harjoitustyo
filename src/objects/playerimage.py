
import os
import pygame
VectorMoving = pygame.math.Vector2

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    """Luokka, joka vastaa pelaajaobjektin koordinaateista,
    liikkumisesta sekä pelaajakuvan lataamisesta.

    Attribuutit:
        self.mainplatform = annetaan Pelaaja-luokalle kopio 
        pelin piirtoluokasta.
        self.user = pelaajaobjektin kuva, joka ladataan kansiosta images
        self.rect =  objektin ulottuvuukseien määrittely
        self.rect.center = määrittää pelaajan aloituskoordinaatit
        Koska pelaajan liikkuminen on toteutettu vektoreiden avulla, 
        tarvitsemme seuraavia muuttujia:
        self.position = pelaajaobjektin paikka näytöllä
        self.velocity = pelaajan vauhti, aluksi paikallaan
        self.acceleration = pelaajan kiihdytysvauhti

    """

    def __init__(self, mainplatform):
        """_summary_
        Args:
        self.mainplatform = annetaan Pelaaja-luokalle kopio 
        pelin piirtoluokasta.
        self.user = pelaajaobjektin kuva, joka ladataan kansiosta images
        self.rect =  objektin ulottuvuukseien määrittely
        self.rect.center = määrittää pelaajan aloituskoordinaatit
        Koska pelaajan liikkuminen on toteutettu vektoreiden avulla, 
        tarvitsemme seuraavia muuttujia:
        self.position = pelaajaobjektin paikka näytöllä
        self.velocity = pelaajan vauhti, aluksi paikallaan
        self.acceleration = pelaajan kiihdytysvauhti
        """
        super().__init__()

        self.mainplatform = mainplatform

        self.user = pygame.image.load(
            os.path.join(dirname, "..", "images", "box.png")
        )

        self.rect = self.user.get_rect()

        self.rect.center = (40, 690)
        self.position = VectorMoving(40, 690)
        self.velocity = VectorMoving(0, 0)
        self.acceleration = VectorMoving(0, 0.0)

    def gravity(self):
        """Vastaa painovoiman toteutuksesta. Tarvitaan, 
        jottei pelaaja lennä ruudun ulkopuolelle.
        """
        self.acceleration = VectorMoving(0, 0.51)

    def events(self, direction):
        """Vastaa pelaajan koordinaattien ja vauhdin
        muuttumisesta. Lisäksi tarkastaa, osuiko
        pelaaja ja hyppytaso toisiinsa. Jos tapahtui osuma, 
        pelaaja ei mene laudan läpi, vaan hyppää sen 
        pinnalta ylös.
        """
        if direction == "right":
            self.acceleration.x += 0.2
        if direction == "left":
            self.acceleration.x -= 0.2

        if direction == "jump":
            self.rect.x += 1
            collision = pygame.sprite.spritecollide(
                self, self.mainplatform.shelves, False)
            self.rect.x -= 1
            if collision:
                self.velocity.y = -15
                collision = False
        self.events2()

    def events2(self):
        """Vastaa nopeuden toteutuksista fysiikan funktioiden avulla.
        Sen jälkeen tarkastellaan x ja y koordinaatteja erikseen.
        Jos x-akseli on alle 0 tai yli 800, se tulee ulos
        toiselta puolelta ikään kuin kiertääkseen peliruutua ympäri.
        Määritellään myös, että objektin x- ja y-koordinaatit toteutuvat
        objektin keskellä alalaidassa, eikä objektin yläkulmassa, kuten 
        normaalisti.
        Lisäksi katsotaan vielä y-koordinaatin paikkaa. Jos se on yli 800, 
        pelaaja on tippunut pelialueen ulkopuolelle, jolloin kutsutaan 
        pelin lopetusfunktiota.
        """
        self.acceleration.y = 0.51
        self.acceleration.x += self.velocity.x * -0.007
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if self.position.x > 840:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = 840

        self.rect.midbottom = self.position

        if self.position.y > 810:
            self.mainplatform.end_game()
