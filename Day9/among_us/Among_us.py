import random
from player import Player, User

class Game:
    def __init__(self, num_players, num_imposters):
        self.num_players = num_players
        self.num_imposters = num_imposters
        self.players = []
        
        roles = ['crewmate'] * (num_players - num_imposters) + ['imposter'] * num_imposters
        random.shuffle(roles)
        
        for i in range(num_players):
            player = Player(i+1, roles[i])
            self.players.append(player)
        
        self.tasks = ['fix wiring', 'align engine output', 'calibrate distributor', 'chart course']
    
    def get_remaining_players(self):
        alive_players = [player for player in self.players if player.alive]
        remaining_player_ids = [player.player_id for player in alive_players]
        return remaining_player_ids
    
    def play(self):
        user_role = input("Do you want to play as a crewmate or an imposter? \n").lower()
        if user_role not in ['crewmate', 'imposter']:
            print("Invalid choice. Defaulting to crewmate.")
            user_role = 'crewmate'

        user_id = self.num_players + 1
        user = User(user_id, user_role)
        self.players.append(user)

        while True:
            # Ask the user if they are a crewmate and whom they suspect as an imposter
            if user.role == 'crewmate' and user.alive:
                suspect_id = input("As a crewmate, whom do you suspect as the imposter? (Enter player ID or 'skip'): ")
                if suspect_id.lower() == 'skip':
                    print("You chose to skip.")
                elif suspect_id.isdigit():
                    suspect_id = int(suspect_id)
                    if any(player.player_id == suspect_id and player.role == 'imposter' for player in self.players):
                        print("Your suspicion was correct! You identified an imposter.")
                    else:
                        print("Your suspicion was incorrect. The player is not an imposter.")
            
            # imposters sabotage and eliminate crewmates
            for player in self.players:
                if player.role == 'imposter' and player.alive:
                    crewmates = [p for p in self.players if p.role == 'crewmate' and p.alive]
                    if crewmates:
                        eliminated = random.choice(crewmates)
                        eliminated.eliminate()
                        print(f'{eliminated} was eliminated by an imposter')
            
            # Ask the user if they are an imposter and whom they want to eliminate
            if user.role == 'imposter' and user.alive:
                target_id = input("As an imposter, whom do you want to eliminate? (Enter player ID or 'skip'): ")
                if target_id.lower() == 'skip':
                    print("You chose to skip.")
                elif target_id.isdigit():
                    target_id = int(target_id)
                    target = next((player for player in self.players if player.player_id == target_id and player.alive), None)
                    if target and target.role == 'crewmate':
                        target.eliminate()
                        print(f'{user} eliminated {target}')
                    else:
                        print("You couldn't eliminate a crewmate.")
            
            # After elimination, print remaining players
            remaining_players = self.get_remaining_players()
            print("Remaining players:", remaining_players)
            
            # check win conditions
            if all(not player.alive for player in self.players if player.role == 'crewmate'):
                imposter_win = any(player.role == 'imposter' and player.alive for player in self.players)
                if imposter_win and self.num_imposters == 1:
                    imposter = next(player for player in self.players if player.role == 'imposter' and player.alive)
                    print(f'Imposters win! The imposter was Player {imposter.player_id}')
                else:
                    print('Imposters win!')
                break
            if all(not player.alive for player in self.players if player.role == 'imposter'):
                print('Crewmates win!')
                break

# create and play game
if __name__ == "__main__":
    game_instance = Game(num_players=10, num_imposters=1)
    game_instance.play()
