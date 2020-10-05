import unittest
from models.result import Result
from models.team import Team
from models.league import League

class TestResult(unittest.TestCase):

    def setUp(self):
        self.league_1 = League("LadsLadsLads", 12)
        self.team_1 = Team("Verdansk Big Thirsters")
        self.team_2 = Team("Nick's Chubb")
        self.result_1 = Result(self.team_1, 101.23, self.team_2, 105.54)
        self.result_2 = Result(self.team_1, 105.54, self.team_2, 101.23)
        self.result_3 = Result(self.team_1, 105.54, self.team_2, 105.54)

    
    def test_result_has_team_1(self):
        self.assertEqual(self.team_1, self.result_1.team_1)


    def test_result_has_team_1_score(self):
        self.assertEqual(101.23, self.result_1.team_1_score)


    def test_result_has_team_2(self):
        self.assertEqual(self.team_2, self.result_1.team_2)

    
    def test_result_has_team_2_score(self):
        self.assertEqual(105.54, self.result_1.team_2_score)


    def test_result_has_id(self):
        self.assertEqual(None, self.result_1.id)

    
    def test_determine_result__team_2_win(self):
        get_winner = self.result_1.determine_result()
        self.assertEqual("Nick's Chubb", get_winner)

    
    def test_determine_result__team_1_win(self):
        get_winner = self.result_2.determine_result()
        self.assertEqual("Verdansk Big Thirsters", get_winner)


    def test_determine_result__draw(self):
        get_winner = self.result_3.determine_result()
        self.assertEqual("Draw", get_winner)

