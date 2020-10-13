from app import ma

class GameDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'num_of_players', 'puzzles','_links')
        ordered = True
        
    puzzles = ma.Nested('PuzzleListSchema', many=True)
    
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_game', id="<id>")}
    )

class GameListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'num_of_players', '_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_game', id="<id>")}
    )
        
game_schema = GameDetailSchema()
games_schema = GameListSchema(many=True)
    
class PuzzleDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'code', 'game_id', 'hints', 'needs', 'holds', '_links')
        ordered = True
        
    hints = ma.Nested('HintListSchema', many=True)
    needs = ma.Nested('ClueListSchema', many=True)
    holds = ma.Nested('ClueListSchema', many=True)
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_puzzle', id="<id>")}
    )
    
class PuzzleListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name','_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_puzzle', id="<id>")}
    )
    
class PuzzleDetailSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'code', 'game_id', 'hints', 'needs', 'holds', '_links')
        ordered = True
        
    hints = ma.Nested('HintListSchema', many=True)
    needs = ma.Nested('ClueListSchema', many=True)
    holds = ma.Nested('ClueListSchema', many=True)
    
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_puzzle_by_game', game_id="<game_id>", puzzle_id="<id>"),
        "detail": ma.URLFor('get_puzzle', id="<id>")
    })
    
class PuzzleListSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name','_links')
        ordered = True
        
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_puzzle_by_game', game_id="<game_id>", puzzle_id="<id>"),
        "detail": ma.URLFor('get_puzzle', id="<id>")
    })
    
puzzle_schema = PuzzleDetailSchema()
puzzles_schema = PuzzleListSchema(many=True)
puzzle_secondary = PuzzleDetailSecondarySchema()
puzzles_secondary = PuzzleListSecondarySchema(many=True)

class HintDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', 'puzzle_id', '_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_hint', id="<id>")}
    )
    
class HintListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', '_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_hint', id="<id>")}
    )
    
class HintDetailSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', 'puzzle_id', '_links')
        ordered = True
        
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_hint_by_puzzle', puzzle_id="<puzzle_id>", hint_id="<id>"),
        "detail": ma.URLFor('get_hint', id="<id>")
    })
    
class HintListSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'text','_links')
        ordered = True
        
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_hint_by_puzzle', puzzle_id="<puzzle_id>", hint_id="<id>"),
        "detail": ma.URLFor('get_hint', id="<id>")
    })
    
hint_schema = HintDetailSchema()
hints_schema = HintListSchema(many=True)
hint_secondary = HintDetailSecondarySchema()
hints_secondary = HintListSecondarySchema(many=True)

class ClueDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'needer', 'holder', '_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_clue', id="<id>")}
    )
    
class ClueListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', '_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_clue', id="<id>")}
    )
    
class ClueDetailSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'needer', 'holder', '_links')
        ordered = True
        
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_clues_by_puzzle', puzzle_id="<holder>", clue_id="<id>"),
        "detail": ma.URLFor('get_clue', id="<id>")
    })
    
class ClueListSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', '_links')
        ordered = True
        
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_clue_by_puzzle', puzzle_id="<holder>", clue_id="<id>"),
        "detail": ma.URLFor('get_clue', id="<id>")
    })
    
clue_schema = ClueDetailSchema()
clues_schema = ClueListSchema(many=True)
clue_secondary = ClueDetailSecondarySchema()
clues_secondary = ClueListSecondarySchema(many=True)

class EventDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'game_id', 'num_of_players', 'date', 'start_time', 'end_time', '_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_event', id="<id>")}
    )

class EventListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'game_id', 'num_of_players', 'date', '_links')
        ordered = True
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_event', id="<id>")}
    )
        
event_schema = EventDetailSchema()
events_schema = EventListSchema(many=True)