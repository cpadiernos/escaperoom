from flask import render_template, request
from app import app, socketio, db
from flask_socketio import join_room, emit, send
from app.models import Game, Puzzle, Hint, Clue, Event
from app.schemas import (games_schema, game_schema,
    puzzle_schema, puzzles_schema, puzzle_secondary, puzzles_secondary,
    hint_schema, hints_schema, hint_secondary, hints_secondary,
    clue_schema, clues_schema, clue_secondary, clues_secondary,
    event_schema, events_schema)
from datetime import datetime, timedelta

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
    
@socketio.on('event')
def send_hint(data):
    status = data['status']
    emit('event', status, broadcast=True)
    
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
    game.num_of_players = num_of_players

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
    
@app.route('/api/puzzles/<id>/before-puzzles', methods=['GET'])
def get_before_puzzles_by_puzzle(id):
    before_puzzles = Puzzle.query.filter(Puzzle.holds.any(Clue.needer==id)).all()
    return puzzles_schema.jsonify(before_puzzles)
    
@app.route('/api/puzzles/<id>/after-puzzles', methods=['GET'])
def get_after_puzzles_by_puzzle(id):
    after_puzzles = Puzzle.query.filter(Puzzle.needs.any(Clue.holder==id)).all()
    return puzzles_schema.jsonify(after_puzzles)
    
# Hint Routes
@app.route('/api/hints', methods=['GET'])
def get_hints():
    all_hints = Hint.query.all()
    return hints_schema.jsonify(all_hints)
    
@app.route('/api/hints', methods=['POST'])
def add_hint():
    text = request.json['text']
    puzzle_id = request.json['puzzle_id']
    
    new_hint = Hint(text, puzzle_id)
    db.session.add(new_hint)
    db.session.commit()
    return hint_schema.jsonify(new_hint)
    
@app.route('/api/hints/<id>', methods=['GET'])
def get_hint(id):
    hint = Hint.query.filter_by(id=id).first()
    return hint_schema.jsonify(hint)

@app.route('/api/hints/<id>', methods=[('PUT')])
def update_hint(id):
    text = request.json['text']
    puzzle_id = request.json['puzzle_id']
    
    hint = Hint.query.filter_by(id=id).first()
    hint.text = text
    hint.puzzle_id = puzzle_id

    db.session.commit()
    return hint_schema.jsonify(hint)
    
@app.route('/api/hints/<id>', methods=['DELETE'])
def delete_hint(id):
    hint = Hint.query.filter_by(id=id).first()
    db.session.delete(hint)
    db.session.commit()
    return hint_schema.jsonify(hint)
    
# Clue Routes
@app.route('/api/clues', methods=['GET'])
def get_clues():
    all_clues = Clue.query.all()
    return clues_schema.jsonify(all_clues)
    
@app.route('/api/clues', methods=['POST'])
def add_clue():
    name = request.json['name']
    needer = request.json['needer']
    holder = request.json['holder']
    
    new_clue = Clue(name, needer, holder)
    db.session.add(new_clue)
    db.session.commit()
    return clue_schema.jsonify(new_clue)
    
@app.route('/api/clues/<id>', methods=['GET'])
def get_clue(id):
    clue = Clue.query.filter_by(id=id).first()
    return clue_schema.jsonify(clue)
    
@app.route('/api/clues/<id>', methods=[('PUT')])
def update_clue(id):
    name = request.json['name']
    needer = request.json['needer']
    holder = request.json['holder']
    
    clue = Clue.query.filter_by(id=id).first()
    clue.name = name
    clue.needer = needer
    clue.holder = holder
    
    db.session.commit()
    return clue_schema.jsonify(clue)
    
@app.route('/api/clues/<id>', methods=['DELETE'])
def delete_clue(id):
    clue = Clue.query.filter_by(id=id).first()
    db.session.delete(clue)
    db.session.commit()
    return clue_schema.jsonify(clue)
    
# Game and Puzzle Routes
@app.route('/api/games/<game_id>/puzzles', methods=['GET'])
def get_puzzles_by_game(game_id):
    game = Game.query.filter_by(id=game_id).first()
    return puzzles_secondary.jsonify(game.puzzles)
    
@app.route('/api/games/<game_id>/puzzles/<puzzle_id>', methods=['GET'])
def get_puzzle_by_game(game_id, puzzle_id):
    puzzle = Puzzle.query.filter_by(id=puzzle_id, game_id=game_id).first()
    return puzzle_secondary.jsonify(puzzle)
    
# Puzzle and Hint Routes
@app.route('/api/puzzles/<puzzle_id>/hints', methods=['GET'])
def get_hints_by_puzzle(puzzle_id):
    puzzle = Puzzle.query.filter_by(id=puzzle_id).first()
    return hints_secondary.jsonify(puzzle.hints)
    
@app.route('/api/puzzles/<puzzle_id>/hints/<hint_id>', methods=['GET'])
def get_hint_by_puzzle(puzzle_id, hint_id):
    hint = Hint.query.filter_by(id=hint_id, puzzle_id=puzzle_id).first()
    return hint_secondary.jsonify(hint)
    
#Puzzle and Clues Routes
@app.route('/api/puzzles/<puzzle_id>/clues', methods=['GET'])
def get_clues_by_puzzle(puzzle_id):
    puzzle = Puzzle.query.filter_by(id=puzzle_id).first()
    return clues_secondary.jsonify(puzzle.holds)
    
@app.route('/api/puzzles/<puzzle_id>/clues/<clue_id>', methods=['GET'])
def get_clue_by_puzzle(puzzle_id, clue_id):
    clue = Clue.query.filter_by(id=clue_id, holder=puzzle_id).first()
    return clue_secondary.jsonify(clue)
    
# Event Routes
@app.route('/api/events', methods=['GET'])
def get_events():
    all_events = Event.query.all()
    return events_schema.jsonify(all_events)
    
@app.route('/api/events', methods=['POST'])
def add_event():
    game_id = request.json['game_id']
    num_of_players = request.json['num_of_players']
    date = datetime.now().date()
    now = datetime.now().replace(microsecond=0)
    start_time = now.time()
    end_time = (now + timedelta(hours=1)).time()
    
    new_event = Event(game_id, num_of_players, date, start_time, end_time)
    db.session.add(new_event)
    db.session.commit()
    return event_schema.jsonify(new_event)
    
@app.route('/api/events/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).first()
    return event_schema.jsonify(event)
    
@app.route('/api/events/active', methods=['GET'])
def get_active_event():
    today = datetime.now().date()
    time_now = datetime.now().replace(microsecond=0).time()
    event = Event.query.filter_by(date=today).filter(Event.end_time > time_now).first()
    return event_schema.jsonify(event)