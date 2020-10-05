from flask import Flask, Blueprint, redirect, render_template, request
import repos.team_repo as team_repo
import repos.result_repo as result_repo
from models.league import League
from models.team import Team
from models.result import Result

leagues_blueprint = Blueprint("leagues", __name__)

# # INDEX
# @leagues_blueprint.route("/teams")
# def teams():
#     teams = team_repo.select_all()
#     return render_template("/teams/index.html", teams=teams)

# # NEW
# @teams_blueprint.route("/teams/new")
# def add_team():
#     return render_template("/teams/new.html")

# # CREATE
# @teams_blueprint.route("/teams", methods=["POST"])
# def create_team():
#     name = request.form["name"]
#     new_team = Team(name)
#     team_repo.save(new_team)
#     return redirect("/teams")

# # SHOW
# @teams_blueprint.route("/teams/<id>")
# def show_team(id):
#     teams = team_repo.select_all()
#     team_1 = team_repo.select(id)
#     results = team_repo.select_all_team_results(id)

#     return render_template("/teams/show.html", team_1=team_1, results=results, teams=teams)

# # EDIT
# @teams_blueprint.route("/teams/<id>/edit")
# def edit_team(id):
#     team = team_repo.select(id)
#     return render_template('/teams/edit.html', team=team)

# # UPDATE
# @teams_blueprint.route("/teams/<id>", methods=["POST"])
# def update_team(id):
#     name = request.form["name"]
#     team = Team(name, id)
#     team_repo.update(team)
#     return redirect("/teams")