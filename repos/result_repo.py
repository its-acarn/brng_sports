from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.result import Result

import repos.team_repo as team_repo


def save(result):
    sql = "INSERT INTO results (team_1_id, team_1_score, team_2_id, team_2_score) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [result.team_1.id, result.team_1_score, result.team_2.id, result.team_2_score]
    output = run_sql(sql, values)
    id = output[0]['id']
    result.id = id

 
def select_all():
    results = []
    sql = "SELECT * FROM results"
    output = run_sql(sql)
    for row in output:
        team_1 = team_repo.select(row["team_1_id"])
        team_2 = team_repo.select(row["team_2_id"])
        result = Result(team_1, row['team_1_score'], team_2, row['team_2_score'], row['id']) 
        results.append(result)
    return results


def select(id):
    sql = "SELECT * FROM results WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    team_1 = team_repo.select(output["team_1_id"])
    team_2 = team_repo.select(output["team_2_id"])
    result = Result(team_1, output['team_1_score'], team_2, output['team_2_score'], output['id'])
    return result


def delete_all():
    sql = "DELETE  FROM results"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM results WHERE id = %s"
    value = [id]
    run_sql(sql, value)


def update(result):
    sql = "UPDATE results SET (team_1_id, team_1_score, team_2_id, team_2_score) = (%s, %s, %s, %s) WHERE id = %s"
    values = [result.team_1.id, result.team_1_score, result.team_2.id, result.team_2_score, result.id]
    run_sql(sql, values)

