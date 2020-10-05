from flask import Flask, Blueprint, redirect, render_template
from controllers.result_controller import results_blueprint 
from controllers.team_controller import teams_blueprint
from controllers.league_controller import leagues_blueprint

app = Flask(__name__)

app.register_blueprint(results_blueprint)
app.register_blueprint(teams_blueprint)
app.register_blueprint(leagues_blueprint)

@app.route('/')
def home():
    return render_template('home.html')