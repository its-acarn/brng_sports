class League:

    def __init__(self, name, league_size_limit, id=None):
        self.name = name
        self.league_size_limit = league_size_limit
        self.no_of_teams = 0
        self.id = id
            

    def add_team_to_league(self, team):
        if self.league_size_limit == self.no_of_teams:
            return "League is full"
        
        else:
            team.league = self
            self.no_of_teams += 1