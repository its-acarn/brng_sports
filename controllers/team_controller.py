from flask import Flask, Blueprint, redirect, render_template, request
import repos.league_repo as league_repo
import repos.team_repo as team_repo
from models.league import League
from models.team import Team

teams_blueprint = Blueprint("teams", __name__)

# INDEX
@teams_blueprint.route("/teams")
def teams():
    teams = team_repo.select_all()
    return render_template("/teams/index.html", teams=teams)

# NEW
@teams_blueprint.route("/teams/new")
def add_team():
    leagues = league_repo.select_all()
    return render_template("/teams/new.html", leagues=leagues)

# CREATE
@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    league_id = request.form["league_id"]
    league = league_repo.select(league_id)   

    if league.league_size_limit == league.no_of_teams:
        return redirect("/teams") #CHECK THIS FOR UX - USER NEEDS TO KNOW WHY TEAM HASNT BEEN CREATED!!!!
    else:
        name = request.form["name"]
        new_team = Team(name)
        team_repo.save(new_team)

        league.add_team_to_league(new_team)

        team_repo.update(new_team)
        league_repo.update(league)
    
    return redirect("/teams")

# SHOW
@teams_blueprint.route("/teams/<id>")
def show_team(id):
    teams = team_repo.select_all()
    team_1 = team_repo.select(id)

    return render_template("/teams/show.html", teams=teams, team_1=team_1)

# EDIT
@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repo.select(id)
    return render_template('/teams/edit.html', team=team)

# UPDATE
@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    name = request.form["name"]
    team = Team(name, id)
    team_repo.update(team)
    return redirect("/teams")

