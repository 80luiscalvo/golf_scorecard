# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from database import init_db
from models import db, User, Tournament, Hole, Scorecard

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and CORS
init_db(app)
CORS(app)
