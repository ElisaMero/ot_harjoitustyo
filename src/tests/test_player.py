import unittest
from objects.playerimage import Player

class TestPlayer(unittest.TestCase):


    def test_created_with_correct_coordinates(self):
        player = Player()
        self.assertEqual(player.rect.x, 50)