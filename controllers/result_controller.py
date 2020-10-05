from flask import Flask, Blueprint, redirect, render_template, request
import repos.team_repo as team_repo
import repos.result_repo as result_repo
from models.team import Team
from models.result import Result

results_blueprint = Blueprint("results", __name__)

# INDEX
@results_blueprint.route("/results")
def results():
    results = result_repo.select_all()
    print("RESULSTSHSJSJSHSJSJS", results[0].id)
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
    result = request.form["result"]
    new_result = Result(team_1, team_1_score, team_2, team_2_score, result)
    result_repo.save(new_result)
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
    result = request.form["result"]
    new_result = Result(team_1, team_1_score, team_2, team_2_score, result, id)
    result_repo.update(new_result)
    return redirect("/results")
