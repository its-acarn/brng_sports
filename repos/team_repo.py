from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.result import Result


def save(team):
    sql = "INSERT INTO teams (name) VALUES (%s) RETURNING *"
    values = [team.name]
    output = run_sql(sql, values)
    id = output[0]['id']
    team.id = id


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    output = run_sql(sql)

    for row in output:
        team = Team(row['name'], row['id'])
        teams.append(team)
    return teams


def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]
    team = Team(output['name'], output['id'])
    return team


def delete_all():
    sql = "DELETE  FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET (name, league_id, games_played, games_won, games_lost, games_drawn) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.league.id, team.games_played, team.games_won, team.games_lost, team.games_drawn, team.id]
    run_sql(sql, values)


# def select_all_team_results(id):
#     results = []
#     sql = "SELECT results.* FROM results WHERE results.team_1_id = %s OR results.team_2_id = %s"
#     values = [id, id]
#     output = run_sql(sql, values)
#     for row in output:
#         result = Result(row['team_1_id'], row['team_1_score'], row['team_2_id'], row['team_2_score'], row['result'], row['id'])
#         results.append(result)

#     return results
    