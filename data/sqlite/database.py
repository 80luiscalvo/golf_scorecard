# database.py
from flask_sqlalchemy import SQLAlchemy
from models import db

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
