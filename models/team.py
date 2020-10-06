class Team:

    def __init__(self, name, league=None, games_played=0, games_won=0, games_lost=0, games_drawn=0,  id=None):
        self.name = name
        self.league = league
        self.games_played = games_played
        self.games_won = games_won
        self.games_lost = games_lost
        self.games_drawn = games_drawn
        self.id = id

    def total_games_equal_check(self):
        if self.games_played == (self.games_won + self.games_lost + self.games_drawn):
            return "OK"
        else:
            return "ERROR"