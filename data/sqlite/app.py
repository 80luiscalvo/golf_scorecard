# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from database import init_db
from models import db, User, Tournament, Hole, Scorecard

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and enable CORS
init_db(app)
CORS(app)

# Routes

# Register a user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not all(key in data for key in ('username', 'email', 'role', 'password_hash')):
        return jsonify({'error': 'Missing required fields'}), 400
    if data['role'] not in ('player', 'organizer'):
        return jsonify({'error': 'Invalid role'}), 400
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        role=data['role'],
        password_hash=data['password_hash']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Create a tournament
@app.route('/create_tournament', methods=['POST'])
def create_tournament():
    data = request.json
    if not all(key in data for key in ('name', 'date', 'status', 'organizer_id')):
        return jsonify({'error': 'Missing required fields'}), 400
    if data['status'] not in ('open', 'closed'):
        return jsonify({'error': 'Invalid tournament status'}), 400
    
    new_tournament = Tournament(
        name=data['name'],
        date=data['date'],
        status=data['status'],
        organizer_id=data['organizer_id']
    )
    db.session.add(new_tournament)
    db.session.commit()
    return jsonify({'message': 'Tournament created successfully'}), 201

# Add a hole
@app.route('/add_hole', methods=['POST'])
def add_hole():
    data = request.json
    if not all(key in data for key in ('tournament_id', 'hole_number', 'distance_red', 'distance_white', 'distance_blue')):
        return jsonify({'error': 'Missing required fields'}), 400

    new_hole = Hole(
        tournament_id=data['tournament_id'],
        hole_number=data['hole_number'],
        handicap=data.get('handicap', None),
        distance_red=data['distance_red'],
        distance_white=data['distance_white'],
        distance_blue=data['distance_blue']
    )
    db.session.add(new_hole)
    db.session.commit()
    return jsonify({'message': 'Hole added successfully'}), 201

# Submit a scorecard
@app.route('/submit_scorecard', methods=['POST'])
def submit_scorecard():
    data = request.json
    if not all(key in data for key in ('player_id', 'tournament_id', 'scores')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    scores = data['scores'].split(',')
    try:
        scores = list(map(int, scores))
    except ValueError:
        return jsonify({'error': 'Scores must be a list of integers'}), 400

    new_scorecard = Scorecard(
        player_id=data['player_id'],
        tournament_id=data['tournament_id'],
        scores=','.join(map(str, scores)),
        total_score=sum(scores)
    )
    db.session.add(new_scorecard)
    db.session.commit()
    return jsonify({'message': 'Scorecard submitted successfully', 'total_score': new_scorecard.total_score}), 201

# Fetch standings for a tournament
@app.route('/get_standings/<int:tournament_id>', methods=['GET'])
def get_standings(tournament_id):
    scorecards = Scorecard.query.filter_by(tournament_id=tournament_id).all()
    standings = sorted(scorecards, key=lambda x: x.total_score)
    results = [
        {'player_id': sc.player_id, 'total_score': sc.total_score}
        for sc in standings
    ]
    return jsonify(results), 200

# Fetch all tournaments
@app.route('/tournaments', methods=['GET'])
def get_tournaments():
    tournaments = Tournament.query.all()
    results = [
        {
            'id': t.id,
            'name': t.name,
            'date': t.date,
            'status': t.status,
            'organizer_id': t.organizer_id
        } for t in tournaments
    ]
    return jsonify(results), 200

# Fetch tournament details including holes
@app.route('/tournament_details/<int:tournament_id>', methods=['GET'])
def get_tournament_details(tournament_id):
    tournament = Tournament.query.get(tournament_id)
    if not tournament:
        return jsonify({'error': 'Tournament not found'}), 404

    holes = Hole.query.filter_by(tournament_id=tournament_id).all()
    holes_data = [
        {
            'hole_number': h.hole_number,
            'handicap': h.handicap,
            'distance_red': h.distance_red,
            'distance_white': h.distance_white,
            'distance_blue': h.distance_blue
        } for h in holes
    ]

    return jsonify({
        'tournament': {
            'id': tournament.id,
            'name': tournament.name,
            'date': tournament.date,
            'status': tournament.status,
            'organizer_id': tournament.organizer_id
        },
        'holes': holes_data
    }), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
