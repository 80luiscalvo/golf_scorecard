# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'player' or 'organizer'
    password_hash = db.Column(db.String(128), nullable=False)

class Tournament(db.Model):
    __tablename__ = 'tournaments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)  # 'open' or 'closed'
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Hole(db.Model):
    __tablename__ = 'holes'
    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'), nullable=False)
    hole_number = db.Column(db.Integer, nullable=False)
    handicap = db.Column(db.Integer, nullable=True)
    distance_red = db.Column(db.Integer, nullable=False)
    distance_white = db.Column(db.Integer, nullable=False)
    distance_blue = db.Column(db.Integer, nullable=False)

class Scorecard(db.Model):
    __tablename__ = 'scorecards'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'), nullable=False)
    scores = db.Column(db.String, nullable=False)  # Comma-separated scores
    total_score = db.Column(db.Integer, nullable=False)
