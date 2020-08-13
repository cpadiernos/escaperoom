from app import ma

class GameDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'num_of_players', 'puzzles','_links')
        
    puzzles = ma.Nested('PuzzleListSchema', many=True)
    
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_game', id="<id>")}
    )

class GameListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'num_of_players', '_links')
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_game', id="<id>")}
    )
        
game_schema = GameDetailSchema()
games_schema = GameListSchema(many=True)
    
class PuzzleDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'code', 'game_id', '_links')
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_puzzle', id="<id>")}
    )
    
class PuzzleListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name','_links')
        
    _links = ma.Hyperlinks(
        {"self": ma.URLFor('get_puzzle', id="<id>")}
    )
    
class PuzzleDetailSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'code', 'game_id', '_links')
        
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_puzzle_by_game', game_id="<game_id>", puzzle_id="<id>"),
        "detail": ma.URLFor('get_puzzle', id="<id>")
    })
    
class PuzzleListSecondarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name','_links')
        
    _links = ma.Hyperlinks({
        "self": ma.URLFor('get_puzzle_by_game', game_id="<game_id>", puzzle_id="<id>"),
        "detail": ma.URLFor('get_puzzle', id="<id>")
    })
    
puzzle_schema = PuzzleDetailSchema()
puzzles_schema = PuzzleListSchema(many=True)
puzzle_secondary = PuzzleDetailSecondarySchema()
puzzles_secondary = PuzzleListSecondarySchema(many=True)