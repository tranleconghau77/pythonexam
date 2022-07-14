import unittest
from main.player import *

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = player("hau")

    def tearDown(self):
        del self.player

    def test_add_points(self):
        self.player.add_point(60)
        self.assertEqual(self.player.get_points(), 120)

if __name__ == "__main__":
    unittest.main()
