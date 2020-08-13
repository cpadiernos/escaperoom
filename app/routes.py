from flask import render_template, request
from app import app, socketio, db
from flask_socketio import join_room, emit, send
from app.models import Game, Puzzle
from app.schemas import games_schema, game_schema, puzzle_schema, puzzles_schema, puzzle_secondary, puzzles_secondary

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/hint/')
def show_hint():
    return render_template('hint_screen.html')
    
@socketio.on('hint')
def send_hint(data):
    hint = data['hint']
    emit('hint', hint, broadcast=True)
    
# Game Routes
@app.route('/api/games', methods=['GET'])
def get_games():
    all_games = Game.query.all()
    return games_schema.jsonify(all_games)
    
@app.route('/api/games', methods=['POST'])
def add_game():
    name = request.json['name']
    description = request.json['description']
    num_of_players = request.json['num_of_players']
    
    new_game = Game(name, description, num_of_players)
    db.session.add(new_game)
    db.session.commit()
    return game_schema.jsonify(new_game)
    
@app.route('/api/games/<id>', methods=['GET'])
def get_game(id):
    game = Game.query.filter_by(id=id).first()
    return game_schema.jsonify(game)
    
@app.route('/api/games/<id>', methods=[('PUT')])
def update_game(id):
    name = request.json['name']
    description = request.json['description']
    num_of_players = request.json['num_of_players']
    
    game = Game.query.filter_by(id=id).first()
    game.name = name
    game.description = description
    game.numb_of_players = num_of_players

    db.session.commit()
    return game_schema.jsonify(game)
    
@app.route('/api/games/<id>', methods=['DELETE'])
def delete_game(id):
    game = Game.query.filter_by(id=id).first()
    db.session.delete(game)
    db.session.commit()
    return game_schema.jsonify(game)

# Puzzle Routes
@app.route('/api/puzzles', methods=['GET'])
def get_puzzles():
    all_puzzles = Puzzle.query.all()
    return puzzles_schema.jsonify(all_puzzles)
    
@app.route('/api/puzzles', methods=['POST'])
def add_puzzle():
    name = request.json['name']
    code = request.json['code']
    game_id = request.json['game_id']
    
    new_puzzle = Puzzle(name, code, game_id)
    db.session.add(new_puzzle)
    db.session.commit()
    return puzzle_schema.jsonify(new_puzzle)
    
@app.route('/api/puzzles/<id>', methods=['GET'])
def get_puzzle(id):
    puzzle = Puzzle.query.filter_by(id=id).first()
    return puzzle_schema.jsonify(puzzle)

@app.route('/api/puzzles/<id>', methods=[('PUT')])
def update_puzzle(id):
    name = request.json['name']
    code = request.json['code']
    game_id = request.json['game_id']
    
    puzzle = Puzzle.query.filter_by(id=id).first()
    puzzle.name = name
    puzzle.code = code
    puzzle.game_id = game_id

    db.session.commit()
    return puzzle_schema.jsonify(puzzle)
    
@app.route('/api/puzzles/<id>', methods=['DELETE'])
def delete_puzzle(id):
    puzzle = Puzzle.query.filter_by(id=id).first()
    db.session.delete(puzzle)
    db.session.commit()
    return puzzle_schema.jsonify(puzzle)
    
# Game and Puzzle Routes
@app.route('/api/games/<game_id>/puzzles', methods=['GET'])
def get_puzzles_by_game(game_id):
    game = Game.query.filter_by(id=game_id).first()
    return puzzles_secondary.jsonify(game.puzzles)
    
@app.route('/api/games/<game_id>/puzzles/<puzzle_id>', methods=['GET'])
def get_puzzle_by_game(game_id, puzzle_id):
    puzzle = Puzzle.query.filter_by(id=puzzle_id, game_id=game_id).first()
    return puzzle_secondary.jsonify(puzzle)