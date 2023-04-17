import unittest
from objects.playerimage import Player
from start import StartScreen
from mainplatform import PlatformJumpingGame


class TestPlayer(unittest.TestCase):

    def test_created_with_correct_coordinates(self):
        player = Player()
        self.assertEqual(player.rect.x, 40)

    def test_moves_left(self):
        player = Player()
        player.events("left")
        self.assertEqual(player.rect.x, 32)

    def test_moves_right(self):
        player = Player()
        player.events("right")
        self.assertEqual(player.rect.x, 48)

    def test_moves_up(self):
        player = Player()
        player.events("jumping")
        self.assertEqual(player.rect.y, 690)

    def test_collision_event(self):
        main = PlatformJumpingGame()
        main.collision()
        self.assertEqual(main.player.jump_velocity, 20)
    
    
