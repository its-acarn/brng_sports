from db.run_sql import run_sql
from models.team import Team
from models.league import League


def save(league):
    sql = "INSERT INTO leagues (name, league_size_limit, no_of_teams) VALUES (%s, %s, %s) RETURNING *"
    values = [league.name, league.league_size_limit, league.no_of_teams]
    output = run_sql(sql, values)
    id = output[0]['id']
    league.id = id


def select_all():
    leagues = []

    sql = "SELECT * FROM leagues ORDER BY id"
    output = run_sql(sql)

    for row in output:
        league = League(row['name'], row['league_size_limit'], row['no_of_teams'], row['id'])
        leagues.append(league)
    return leagues


def select(id):
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]
    league = League(output['name'], output['league_size_limit'], output['no_of_teams'], output['id'])
    return league


def delete_all():
    sql = "DELETE  FROM leagues"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(league):
    sql = "UPDATE leagues SET (name, league_size_limit, no_of_teams) = (%s, %s, %s) WHERE id = %s"
    values = [league.name, league.league_size_limit, league.no_of_teams, league.id]
    run_sql(sql, values)
