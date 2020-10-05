import pdb

from models.league import League
from models.team import Team
from models.result import Result

from repos import result_repo, team_repo, league_repo

league_1 = League("LadsLadsLads", 12)
league_repo.save(league_1)

# result_repo.delete_all()
# team_repo.delete_all()

team_1 = Team("Verdansk Big Thirsters")
team_repo.save(team_1)

team_2 = Team("Nick's Chubb")
team_repo.save(team_2)

team_3 = Team("Go Wentz I Came!")
team_repo.save(team_3)

# team_4 = Team("Big Trumple in Lil China")
# team_repo.save(team_4)

result_1 = Result(team_1, 104.32, team_2, 102.68)
result_repo.save(result_1)
# result_2 = Result(team_3, 148.04, team_4, 99.22, True)
# result_repo.save(result_2)
# result_3 = Result(team_3, 132.14, team_1, 88.02, True)
# result_repo.save(result_3)
# result_4 = Result(team_4, 167.86, team_2, 99.89, True)
# result_repo.save(result_4)
# result_5 = Result(team_4, 132.76, team_1, 111.66, True)
# result_repo.save(result_5)

pdb.set_trace()