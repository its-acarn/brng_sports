import unittest
from models.team import Team
from models.league import League

class TestLeague(unittest.TestCase):

    def setUp(self):
        self.league_1 = League("LadsLadsLads", 12)
        self.team_1 = Team("Verdansk Big Thirsters")
        self.team_2 = Team("Nick's Chubb")

    
    def test_league_has_name(self):
        self.assertEqual("LadsLadsLads", self.league_1.name)


    def test_league_has_league_size_limit(self):
        self.assertEqual(12, self.league_1.league_size_limit) 

    
    def test_league_has_id(self):
        self.assertEqual(None, self.league_1.id)


    def test_add_team_to_league(self):
        self.league_1.add_team_to_league(self.team_1)
        self.assertEqual(1, self.league_1.no_of_teams)


    def test_add_team_to_league__two_teams(self):
        self.league_1.add_team_to_league(self.team_1)
        self.league_1.add_team_to_league(self.team_2)
        self.assertEqual(2, self.league_1.no_of_teams)
    