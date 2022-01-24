import HTMLTestRunner
import unittest
from unittest.result import failfast
from cached_data import *


class TestGameStartupData(unittest.TestCase):
    def setUp(self):
        self.util = util
        if not check_cached_data():
            exit()


class TestLoadTeam(TestGameStartupData):
    def test_load_team_1(self):
        '''
        Test the number of team loaded
        '''
        self.assertEqual(len(self.util.teamDic), 5)
        self.assertNotEqual(len(self.util.teamDic), 4)

    def test_load_team_2(self):
        '''
        Check The Team Value in the cached data
        '''
        team_list = ['IND', 'AUS', 'ENG', 'SA', 'WI']

        for key in team_list:
            self.assertIn(key, self.util.teamDic.keys())

    def test_load_team_3(self):
        '''
        Checking the team length not equal to zero
        '''
        self.assertNotEqual(len(self.util.teamDic), 0)


class TestLoadBowler(TestGameStartupData):
    def test_load_bowler_data_1(self):
        '''
        Test the number of bowler data count
        '''
        self.assertEqual(len(self.util.bowlerDic), len(self.util.teamDic))

    def test_load_bowler_data_2(self):
        '''
        Test the number of bowler with team code
        '''
        team_list = ['IND', 'AUS', 'ENG', 'SA', 'WI']

        for key in team_list:
            self.assertIn(key, self.util.bowlerDic.keys())

    def test_load_bowler_data_3(self):
        '''
        Check the instance of the class return by the cached data of bowler
        '''

        for k, v in self.util.bowlerDic.items():
            self.assertIsInstance(v, TeamClass)

    def test_load_bowler_data_4(self):
        '''
        Check the count of bowler in each team
        '''

        for k, v in self.util.bowlerDic.items():
            self.assertEqual(len(v.bowler_list), 4)


class TestLoadBowl(TestGameStartupData):
    def test_load_bowl_data_1(self):
        '''
        Check the bowl data not null
        '''
        self.assertNotEqual(len(self.util.pace_bowl_data), 0)
        self.assertNotEqual(len(self.util.spin_bowl_data), 0)


class TestLoadPlayer(TestGameStartupData):
    def test_load_player_data_1(self):
        '''
        Check the player data load as cache
        '''
        self.assertNotEqual(len(self.util.player_data), 0)

    def test_load_player_data_2(self):
        '''
        Check the player data load as cache
        '''
        list_gameid = [90, 91]

        for key in list_gameid:
            self.assertIn(str(key), self.util.player_data.keys())


class TestLoadSession(TestGameStartupData):
    def test_load_session_data_1(self):
        '''
        Check the player session load as cache
        '''
        self.assertNotEqual(len(self.util.session), 0)

    def test_load_session_data_2(self):
        '''
        Check the session object instance class
        '''
        for k, v in self.util.session.items():
            self.assertIsInstance(v, Session)

    def test_load_session_data_3(self):
        '''
        Check the status in session object
        '''
        for k, v in self.util.session.items():
            self.assertEqual(v.status, constants.UNFINISHED)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='test-report'),failfast=False, buffer=False)