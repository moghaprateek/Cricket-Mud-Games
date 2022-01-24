from utility_functions import *
import unittest


class TestUtility(unittest.TestCase):
    def test_reload_player_details_1(self):
        reload_player_data()
        self.assertNotEqual(len(player_data), 0)

    def test_reload_player_details_2(self):
        reload_player_data()
        game_id = [90, 91]
        for games in game_id:
            self.assertIn(games, player_data.keys())

    def test_verify_game_id(self):
        game_id = [90, 91]
        for games in game_id:
            self.assertTrue(verify_game_id(games))


if __name__ == '__main__':
    unittest.main()
