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

    new_result = Result(team_1, team_1_score, team_2, team_2_score)
    result_repo.save(new_result)
    new_result.determine_result()
    

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
    result.team_1 = team_1
    result.team_1_score = team_1_score
    result.team_2 = team_2
    result.team_2_score = team_2_score

    result.determine_result()#WRONG FUNCTION TO USE WHEN UPDATING RESULTS AS IT KEEPS ADDING GAMES INSTEAD OF REPLACING VALUES

    team_repo.update(team_1)
    team_repo.update(team_2)
    result_repo.update(result)

    return redirect("/results")
