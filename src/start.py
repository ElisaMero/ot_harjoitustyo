
import sys
import pygame


class StartScreen:
    def __init__(self):
        self.screen2 = pygame.display.set_mode((840, 780))

    def startloop(self):
        while True:
            self.graphics2()
            break
        return

    def graphics2(self):
        while True:
            pygame.display.set_caption("Jumping Game")
            self.screen2.fill((173, 255, 255))

            pygame.draw.circle(self.screen2, (255, 255, 255), (100, 100), 20)
            pygame.draw.circle(self.screen2, (255, 255, 255), (150, 100), 20)
            pygame.draw.circle(self.screen2, (255, 255, 255), (125, 85), 20)
            pygame.draw.circle(self.screen2, (255, 255, 255), (125, 100), 20)

            pygame.draw.rect(self.screen2, (249, 194, 240),
                             (220, 340, 430, 210))
            font = pygame.font.SysFont("Arial", 90)
            font2 = pygame.font.SysFont("Arial", 60)
            text = font.render("Start", True, (255, 255, 255))
            text2 = font2.render("Press ENTER to start", True, (255, 255, 255))
            self.screen2.blit(text, (310, 380))
            self.screen2.blit(text2, (70, 180))
            pygame.display.flip()
            pygame.display.update()
            self.startgame()
            return

    def startgame(self):
        clock = pygame.time.Clock()

        while True:
            for happens in pygame.event.get():
                if happens.type == pygame.QUIT:
                    sys.exit()

                if happens.type == pygame.KEYDOWN:
                    return

                clock.tick(60)
