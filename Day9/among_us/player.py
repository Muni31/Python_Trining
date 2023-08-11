class Player:
    def __init__(self, player_id, role):
        self.player_id = player_id
        self.role = role
        self.alive = True
    
    def eliminate(self):
        self.alive = False
    
    def __str__(self):
        return f'Player {self.player_id} ({self.role})'

class User(Player):
    def __init__(self, player_id, role):
        super().__init__(player_id, role)
