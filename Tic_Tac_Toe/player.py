import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random spot for computer's next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn, please move(0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print ('Invalid square, Try again')
        return val 

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #choose randomly
        else:
            square = self.minimax(game, self.letter)['position'] # otherwise choose a square based on the minimax principle 
        return square

    def minimax(self, state, player):
        other_player = 'O' if player == 'X' else 'X' # other_player is the opposite of player
        max_player = self.letter #yourself 
        # tips, when we want to use a recursion. we need to have a base case, that is the end of of the recursion

        # first we need to check if the previous move is a winnier
        if state.current_winner == other_player:
            # we should return position and score because we need to keep track of the score
            # for minimax to work
            return {'position': None, 
                    'score': 1*(state.num_empty_squares()+1) if other_player == max_player else -1*(
                                state.num_empty_squares()+1)} # if there is no +1 here, even there is a winner, the statenumber still could be 0 
        
        elif not state.empty_squares():
            return {'position': None,
                    'score': 0} 

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each step to get the score lager
        else: 
            best = {'position': None, 'score': math.inf} # each step to get the score smaller
        
        for possible_move in state.available_moves():
            # step 1: make a move, try the square
            state.make_move(possible_move, player)
            # step 2: rescurse using minimax after making that move.
            sim_score = self.minimax(state, other_player) # it will automatically check if the previous move is a winner or not
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best





