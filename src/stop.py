
import sys
import pygame


class StopScreen:
    def __init__(self):
        self.screen3 = pygame.display.set_mode((840, 780))

    def last_loop(self):
        self.last_graphics()

    def last_graphics(self):

        pygame.display.set_caption("Jumping Game")
        self.screen3.fill((173, 255, 255))
        pygame.draw.circle(self.screen3, (255, 255, 255), (100, 100), 20)
        pygame.draw.circle(self.screen3, (255, 255, 255), (150, 100), 20)
        pygame.draw.circle(self.screen3, (255, 255, 255), (125, 85), 20)
        pygame.draw.circle(self.screen3, (255, 255, 255), (125, 100), 20)

        pygame.draw.rect(self.screen3, (249, 194, 240),
                         (220, 340, 430, 210))
        font = pygame.font.SysFont("Arial", 90)
        text = font.render("Game Over", True, (255, 255, 255))
        self.screen3.blit(text, (230, 380))
        pygame.display.flip()
        pygame.display.update()
        self.stop_game()

    def stop_game(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            pygame.display.update()

            for happens in pygame.event.get():
                if happens.type == pygame.QUIT:
                    run = False
                    sys.exit()

                clock.tick(60)
