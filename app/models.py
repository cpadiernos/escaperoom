from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(100))
    num_of_players = db.Column(db.Integer)
    puzzles = db.relationship('Puzzle', backref='game', lazy=True)
    
    def __repr__(self):
        return f'{self.name}'
    
class Puzzle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    code = db.Column(db.String(100), unique=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    
    def __repr__(self):
        return f'{self.name}'
