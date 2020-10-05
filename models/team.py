class Team:

    def __init__(self, name, league=None, id=None):
        self.name = name
        self.league = league
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.games_drawn = 0
        self.id = id

    def total_games_equal_check(self):
        if self.games_played == (self.games_won + self.games_lost + self.games_drawn):
            return "OK"
        else:
            return "ERROR"