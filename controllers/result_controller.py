from flask import Flask, Blueprint, redirect, render_template, request
import repos.league_repo as league_repo
import repos.team_repo as team_repo
import repos.result_repo as result_repo
from models.team import Team
from models.result import Result

results_blueprint = Blueprint("results", __name__)

# INDEX
@results_blueprint.route("/results")
def results():
    results = result_repo.select_all()
    return render_template("/results/index.html", results=results)

# NEW
@results_blueprint.route("/result/new")
def new_result():
    teams = team_repo.select_all()
    return render_template("/results/new.html", teams=teams)

# CREATE
@results_blueprint.route("/results", methods=["POST"])
def create_result():
    team_1_id = request.form["team_1_id"]
    team_1 = team_repo.select(team_1_id)
    team_1_score = request.form["team_1_score"]

    team_2_id = request.form["team_2_id"]
    team_2 = team_repo.select(team_2_id)
    team_2_score = request.form["team_2_score"]

    print("team1score", team_1_score, "team2score", team_2_score)

    new_result = Result(team_1, team_1_score, team_2, team_2_score)
    result_repo.save(new_result)
    
    if int(team_1_score) > int(team_2_score):
        team_1.games_played += 1
        team_1.games_won += 1

        team_2.games_played += 1
        team_2.games_lost += 1
        print("11111111111111111111111111111")
        # import pdb; pdb.set_trace()
    elif int(team_1_score) < int(team_2_score):
        team_1.games_played += 1
        team_1.games_lost += 1

        team_2.games_played += 1
        team_2.games_won += 1
        print("2222222222222222222222222222")

    else:
        team_1.games_played += 1
        team_1.games_drawn += 1

        team_2.games_played += 1
        team_2.games_drawn += 1
        print("3333333333333333333333333")

    team_repo.update(team_1)
    team_repo.update(team_2)

    return redirect("/results")

# SHOW
@results_blueprint.route("/results/<id>")
def show_result(id):
    result = result_repo.select(id)
    return render_template("/results/show.html", result=result)

# EDIT
@results_blueprint.route("/results/<id>/edit")
def edit_result(id):
    results = result_repo.select_all()
    teams = team_repo.select_all()
    result = result_repo.select(id)
    return render_template('/results/edit.html', result=result, results=results, teams=teams)

# UPDATE
@results_blueprint.route("/results/<id>", methods=["POST"])
def update_result(id):
    team_1_id = request.form["team_1_id"]
    team_1 = team_repo.select(team_1_id)
    team_1_score = request.form["team_1_score"]

    team_2_id = request.form["team_2_id"]
    team_2 = team_repo.select(team_2_id)
    team_2_score = request.form["team_2_score"]

    result = result_repo.select(id)

    winner = result.get_winner()
    print("############################", winner.name)
    print("############################", result.team_1.name)
    print("############################", result.team_2.name)


    if (winner == result.team_1) :
        team_1.games_played -= 1
        team_1.games_won -= 1 
        team_2.games_played -= 1
        team_2.games_lost -= 1 

    elif (winner == result.team_2) :
        team_1.games_played -= 1
        team_1.games_lost -= 1 
        team_2.games_played -= 1
        team_2.games_won -= 1 

    else:
        team_1.games_played -= 1
        team_2.games_played -= 1
        result.team_1.games_drawn -= 1
        result.team_2.games_drawn -= 1

    result.team_1 = team_1
    result.team_1_score = team_1_score
    result.team_2 = team_2
    result.team_2_score = team_2_score

    winner = result.get_winner()
    print("############################", winner.name)
    print("############################", team_1.name)
    print("############################", team_2.name)


    if (winner == team_1) :
        team_1.games_played += 1
        team_1.games_won += 1 
        team_2.games_played += 1
        team_2.games_lost += 1 

    elif (winner == team_2) :
        team_1.games_played += 1
        team_1.games_lost += 1 
        team_2.games_played += 1
        team_2.games_won += 1 

    else:
        team_1.games_played += 1
        team_2.games_played += 1
        result.team_1.games_drawn += 1
        result.team_2.games_drawn += 1

    team_repo.update(team_1)
    team_repo.update(team_2)
    result_repo.update(result)

    return redirect("/results")
