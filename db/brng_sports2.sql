DROP TABLE results;
DROP TABLE teams;
DROP TABLE leagues;

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    league_size_limit INT,
    no_of_teams INT
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    league_id INT REFERENCES leagues(id),
    games_played INT,
    games_won INT,
    games_lost INT,
    games_drawn INT
);

CREATE TABLE results (
    id SERIAL PRIMARY KEY,
    team_1_id INT REFERENCES teams(id),
    team_1_score FLOAT(4),
    team_2_id INT REFERENCES teams(id),
    team_2_score FLOAT(4)
);