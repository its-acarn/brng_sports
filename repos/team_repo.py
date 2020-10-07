from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.result import Result
import repos.league_repo as league_repo


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
        league = league_repo.select(row["league_id"])
        team = Team(row['name'], row['games_played'], row['games_won'], row['games_lost'], row['games_drawn'], league, row['id'])
        teams.append(team)
    return teams


def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]
    
    league = league_repo.select(output["league_id"])
    team = Team(output['name'], output['games_played'], output['games_won'], output['games_lost'], output['games_drawn'], league, output['id'])
    return team


def delete_all():
    sql = "DELETE  FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET (name, games_played, games_won, games_lost, games_drawn, league_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.games_played, team.games_won, team.games_lost, team.games_drawn, team.league.id, team.id]
    run_sql(sql, values)

def select_all_ranked():
    teams = []
    sql = "SELECT *, RANK() OVER (ORDER BY games_won DESC, games_drawn DESC, name ASC) AS rank FROM teams ORDER BY rank"
    output = run_sql(sql)

    for row in output:
        league = league_repo.select(row["league_id"])
        team = Result(output['name'], output['games_played'], output['games_won'], output['games_lost'], output['games_drawn'], league, output['id'])
        teams.append(result)

    return teams

