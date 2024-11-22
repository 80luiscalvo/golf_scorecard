# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///golf_tournament.db'  # SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  # Use a secure key for sessions
