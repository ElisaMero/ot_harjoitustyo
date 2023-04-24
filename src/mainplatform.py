
import sys
from random import randint
import pygame
from objects.playerimage import Player
from objects.shelves import Shelves
from objects.candies import Candies


class PlatformJumpingGame():
    def __init__(self):

        self.screen = pygame.display.set_mode((840, 780))

        self.player = Player(self)
        self.jumping = False
        self.calculator = 0
        self.all_sprites = pygame.sprite.Group()
        self.shelves = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def loop(self):
        while True:
            self.background()
            self.draw_all()
            self.collisions()
            self.candy_collision()
            self.score()
            self.player.gravity()
            self.moving()
            self.clock.tick(60)

    def background(self):
        pygame.display.update()
        pygame.display.set_caption("Jumping Game")
        self.screen.fill((173, 255, 255))
        # clouds:
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
        # sign:
        pygame.draw.rect(self.screen, (149, 113, 85), (375, 710, 73, 33))
        pygame.draw.rect(self.screen, (149, 113, 85), (400, 715, 10, 60))
        font = pygame.font.SysFont("Arial", 20)
        text1 = font.render("Danger!", True, (255, 255, 255))
        self.screen.blit(text1, (376, 715))

        self.player.gravity()
        self.collisions()
        self.candy_collision()
        self.draw_all()
        self.score()

    def add_sprites(self):
        self.sprite_add_player()
        self.draw_surfaces()
        self.draw_candy()
        self.loop()

    def sprite_add_player(self):
        self.all_sprites.add(self.player)

    def draw_surfaces(self):
        shelf1 = Shelves(560, 640, 130, 20)
        shelf2 = Shelves(100, 200, 130, 20)
        shelf3 = Shelves(0, 760, 290, 20)    # floor1
        shelf4 = Shelves(530, 370, 130, 20)
        shelf5 = Shelves(390, 760, 480, 20)  # floor2
        shelf6 = Shelves(100, 490, 130, 20)
        shelf7 = Shelves(400, 270, 130, 20)
        self.add_in_all_sprites(shelf1, shelf2, shelf3,
                                shelf4, shelf5, shelf6, shelf7)

    def add_in_all_sprites(self, shelf1, shelf2, shelf3, shelf4, shelf5, shelf6, shelf7):
        self.all_sprites.add(shelf1)
        self.all_sprites.add(shelf2)
        self.all_sprites.add(shelf3)
        self.all_sprites.add(shelf4)
        self.all_sprites.add(shelf5)
        self.all_sprites.add(shelf6)
        self.all_sprites.add(shelf7)
        self.add_in_shelves(shelf1, shelf2, shelf3,
                            shelf4, shelf5, shelf6, shelf7)

    def add_in_shelves(self, shelf1, shelf2, shelf3, shelf4, shelf5, shelf6, shelf7):
        self.shelves.add(shelf1)
        self.shelves.add(shelf2)
        self.shelves.add(shelf3)
        self.shelves.add(shelf4)
        self.shelves.add(shelf5)
        self.shelves.add(shelf6)
        self.shelves.add(shelf7)
        pygame.display.update()

    def draw_candy(self):
        self.candysprite = pygame.sprite.Group()
        test = Candies(randint(15, 600), randint(15, 630), 15, 20)
        self.all_sprites.add(test)
        self.candysprite.add(test)

    def draw_all(self):
        self.player.gravity()
        self.shelves.draw(self.screen)
        self.candysprite.draw(self.screen)
        self.screen.blit(self.player.user, (self.player.rect.center))
        self.all_sprites.update()
        pygame.display.flip()

    def collisions(self):
        collision = pygame.sprite.spritecollide(
            self.player, self.shelves, False)
        if collision:
            self.player.position.y = collision[0].rect.top
            self.player.acceleration.y = 0
            self.player.position.y = collision[0].rect.top

    def candy_collision(self):
        collision2 = pygame.sprite.spritecollide(
            self.player, self.candysprite, False)
        if collision2:
            self.player.position.y = collision2[0].rect.top
            self.counter()
        else:
            pass

    def counter(self):
        self.calculator1()
        self.score()
        self.draw_candy()

    def calculator1(self):
        self.calculator += 1

    def score(self):
        font = pygame.font.SysFont("Arial", 40)
        text = font.render(f"Score: {self.calculator}", True, (255, 255, 255))
        self.screen.blit(text, (630, 80))
        pygame.display.flip()
        pygame.display.update()

    def moving(self):
        self.draw_all()
        while True:
            pygame.display.update()
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
            if self.jumping is False and usercontrol[pygame.K_SPACE]:
                self.jumping = True
            if self.jumping:
                self.player.events("jump")
                if self.player.velocity == 15:
                    self.jumping = False
                    self.draw_surfaces()

            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(20)
