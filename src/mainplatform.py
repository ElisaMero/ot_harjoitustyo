
import sys
import pygame
from objects.playerimage import Player


class PlatformJumpingGame():
    def __init__(self):

        self.screen = pygame.display.set_mode((840, 780))

        self.player = Player()

        self.jumping = False

        self.x = 590
        self.y = 650

    def loop(self):
        while True:
            self.background()
            self.moving()

    def background(self):
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
        self.draw_surfaces()

    def draw_surfaces(self):
        surface1 = pygame.draw.rect(
            self.screen, (246, 202, 161), (self.x, self.y, 130, 20))
        pygame.display.update()
        self.draw_player()

    def draw_player(self):
        self.screen.blit(self.player.user,
                         (self.player.rect.x, self.player.rect.y))
        self.player.all_sprites.draw(self.screen)
        pygame.display.update()

    def collision(self):
        player_bottom = ((self.player.rect.x + 10), (self.player.rect.y+20))
        if self.x + 130 >= player_bottom[0] >= self.x:
            self.player.jump_velocity = 0
            self.jumping = False
        pygame.display.update()

    def moving(self):
        clock = pygame.time.Clock()

        while True:
            pygame.display.update()
            self.background()
            for happens in pygame.event.get():
                if happens.type == pygame.QUIT:
                    sys.exit()

            usercontrol = pygame.key.get_pressed()

            if usercontrol[pygame.K_RIGHT]:
                self.player.events("right")
                self.draw_player()
            if usercontrol[pygame.K_LEFT]:
                self.player.events("left")
                self.draw_player()

            if self.jumping is False and usercontrol[pygame.K_SPACE]:
                self.jumping = True
            if self.jumping:
                self.player.events("jump")
                self.collision()
                if self.player.jump_velocity == 20:
                    self.draw_surfaces()
                    self.jumping = False

            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(20)
            clock.tick(60)
