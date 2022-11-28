class Team():
    def __init__(self, input_team_name, input_list_of_players, input_coach_name):
        self.name = input_team_name
        self.players = input_list_of_players
        self.coach = input_coach_name
        self.points = 0
    
    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, player_name):
        for name in self.players:
            if name == player_name:
                return True 
        return False

    def play_game(self, winning_points):
        if winning_points == True:
            self.points += 3
        else:
            False
        # return points
    
