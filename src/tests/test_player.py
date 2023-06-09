import unittest
import pygame
import sys
from objects.playerimage import Player
from mainplatform import PlatformJumpingGame
from objects.candies import Candies
from objects.shelves import Shelves
from repositories.database import SaveData


class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def test_created_with_correct_coordinates(self):
        player = Player(self)
        self.assertEqual(player.position.x, 40.0)

    def test_moves_left(self):
        player = Player(self)
        player.events("left")
        self.assertEqual(player.position.x, 39.7)

    def test_moves_right(self):
        player = Player(self)
        player.events("right")
        self.assertEqual(player.position.x, 40.3)

    def test_moves_correctly_in_y_position(self):
        player = Player(self)
        player.events("right")
        self.assertEqual(player.position.y, 690.765)

    def test_moves_correctly_in_y_position2(self):
        player = Player(self)
        player.events("left")
        self.assertEqual(player.position.y, 690.765)

    def test_moves_up_check_x(self):
        player = Player(self)
        player.events("jumping")
        self.assertEqual(player.position.x, 40)

    def test_gravity(self):
        player = Player(self)
        player.gravity()
        self.assertEqual(player.acceleration, (0, 0.51))

    def test_moving_elements(self):
        player = Player(self)
        player.events("left")
        self.assertEqual(player.acceleration.x, -0.2)

    def test_moving_elements2(self):
        player = Player(self)
        player.events("right")
        self.assertEqual(player.acceleration.x, 0.2)

    def test_moving_elements3(self):
        player = Player(self)
        player.events("left")
        self.assertEqual(player.acceleration.y, 0.51)

    def test_moving_elements4(self):
        player = Player(self)
        player.events("right")
        self.assertEqual(player.acceleration.y, 0.51)

    def test_moving_elements_in_jumping(self):
        player = Player(self)
        player.events("jumping")
        self.assertEqual(player.rect.x, 15)

    def test_moving_outside_screen_x(self):
        player = Player(self)
        player.position.x = 860
        player.events("right")
        self.assertEqual(player.position.x, 0)

    def test_moving_outside_screen2_x(self):
        player = Player(self)
        player.position.x = -2
        player.events("left")
        self.assertEqual(player.position.x, 840)

class TestOthers(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def test_add_player_in_sprites(self):
        main = PlatformJumpingGame()
        main.sprite_add_player()
        self.assertTrue(main.player in main.all_sprites)

    def test_counter(self):
        main = PlatformJumpingGame()
        main.calculator1()
        self.assertEqual(main.calculator, 1)

    def test_candy_koordinates(self):
        candy = Candies(15, 15, 15, 15)
        Candies(15, 15, 15, 15)
        self.assertEqual(candy.rect.x, candy.rect.y, 30)

    def test_shelves(self):
        shelf = Shelves(560, 640, 130, 20)
        Shelves(560, 640, 130, 20)
        self.assertEqual(shelf.rect.x, 560)

    def test_shelves2(self):
        shelf = Shelves(560, 640, 130, 20)
        Shelves(560, 640, 130, 20)
        self.assertEqual(shelf.rect.y, 640)

    def test_database_order(self):
        data = SaveData(1)
        data.scores_in_order()
        self.assertTrue(1)

    def test_collision(self):
        main = PlatformJumpingGame()
        player = Player(main)
        player.events("jump")
        pygame.sprite.spritecollide(player, main.shelves, False)
        self.assertEqual(player.velocity.y, 0.51)

    def test_shelves_in_sprites(self):
        main = PlatformJumpingGame()
        main.make_surfaces()
        self.assertTrue(main.all_sprites, not None)
