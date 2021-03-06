class Result:

    def __init__(self, team_1, team_1_score, team_2, team_2_score, id=None):
        self.team_1 = team_1
        self.team_1_score = team_1_score
        self.team_2 = team_2
        self.team_2_score = team_2_score
        self.id = id


    def determine_result(self):
        if float(self.team_1_score) > float(self.team_2_score):
            self.team_1.games_played += 1
            self.team_1.games_won += 1
            self.team_2.games_played += 1
            self.team_2.games_lost += 1

        elif float(self.team_2_score) > float(self.team_1_score):
            self.team_2.games_played += 1
            self.team_2.games_won += 1
            self.team_1.games_played += 1
            self.team_1.games_lost += 1
        
        else:
            self.team_1.games_played += 1
            self.team_2.games_played += 1
            self.team_1.games_drawn += 1
            self.team_2.games_drawn += 1


    def get_winner(self):
        if float(self.team_1_score) > float(self.team_2_score):
            winner = self.team_1
            return winner

        elif float(self.team_2_score) > float(self.team_1_score):
            winner = self.team_2
            return winner

        else:
            return None


    def reverse_result(self):
        if float(self.team_1_score) > float(self.team_2_score):
            self.team_1.games_played -= 1
            self.team_1.games_won -= 1
            self.team_2.games_played -= 1
            self.team_2.games_lost -= 1

        elif float(self.team_2_score) > float(self.team_1_score):
            self.team_2.games_played -= 1
            self.team_2.games_won -= 1
            self.team_1.games_played -= 1
            self.team_1.games_lost -= 1
        
        else:
            self.team_1.games_played -= 1
            self.team_2.games_played -= 1
            self.team_1.games_drawn -= 1
            self.team_2.games_drawn -= 1 
