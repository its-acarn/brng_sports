from flask import Flask, Blueprint, redirect, render_template, request
import repos.league_repo as league_repo
import repos.team_repo as team_repo
import repos.result_repo as result_repo
from models.league import League
from models.team import Team
from models.result import Result

leagues_blueprint = Blueprint("leagues", __name__)

# INDEX
@leagues_blueprint.route("/leagues")
def leagues():
    leagues = league_repo.select_all()
    return render_template("/leagues/index.html", leagues=leagues)

# NEW
@leagues_blueprint.route("/league/new")
def add_league():
    return render_template("/leagues/new.html")

# CREATE
@leagues_blueprint.route("/leagues", methods=["POST"])
def create_leagues():

    name = request.form["name"]
    league_size_limit = request.form["league_size_limit"]
    new_league = League(name, league_size_limit)
    league_repo.save(new_league)
    league_repo.update(new_league)
    
    return redirect("/leagues")

# SHOW
@leagues_blueprint.route("/leagues/<id>")
def show_league(id):
    leagues = league_repo.select_all()
    league = league_repo.select(id)
    #ADD IN LEAGUE TEAMS
    return render_template("/leagues/show.html", leagues=leagues, league=league)

# EDIT
@leagues_blueprint.route("/leagues/<id>/edit")
def edit_league(id):
    league = league_repo.select(id)
    return render_template('/leagues/edit.html', league=league)

# UPDATE
@leagues_blueprint.route("/leagues/<id>", methods=["POST"])
def update_league(id):
    league = league_repo.select(id)
    name = request.form["name"]
    league_size_limit = request.form["league_size_limit"]
    league.name = name
    league.league_size_limit = league_size_limit
    league_repo.update(league)
    return redirect("/leagues")