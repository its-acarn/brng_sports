import unittest
from models.team import Team
from models.league import League

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.league_1 = League("LadsLadsLads", 12)
        self.team_1 = Team("Nick's Chubb")

    
    def test_team_has_name(self):
        self.assertEqual("Nick's Chubb", self.team_1.name)

    
    def test_team_has_league(self):
        self.assertEqual(None, self.team_1.league)


    def test_team_has_id(self):
        self.assertEqual(None, self.team_1.id)

    
    def test_team_has_games_won(self):
        self.assertEqual(0, self.team_1.games_won)


    def test_team_has_games_lost(self):
        self.assertEqual(0, self.team_1.games_lost)


    def test_team_has_games_drawn(self):
        self.assertEqual(0, self.team_1.games_drawn)

    
    def test_total_games_equal_check(self):
        get_check = self.team_1.total_games_equal_check()
        self.assertEqual("OK", get_check)