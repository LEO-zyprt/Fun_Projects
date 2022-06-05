from player import HumanPlayer, RandomComputerPlayer
import random
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)] # we will use a single list to rep a 3*3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ', ' | '.join(row), ' |')

    @staticmethod
    # give a number list for player to refer
    def print_board_nums():
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| ', ' | '.join(row), ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # # we need to return a list to let player know which is the available for the next move
        # moves = []
        # for (i, spot) in enumerate(self.board):
        # # enumerate: [o,x,x] --> [(0,o),(1,x),(2,x)]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves  
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count('  ')
        # or return len(self.available_moves())

    def winner(self, square, letter):
        # first, to check if the winner exists in the row
        row_ind = square // 3
        row = self.board[3*row_ind:3*(row_ind+1)]
        if all([spot == letter for spot in row]):
            return True

        # Second, to check if the winner exists in the column
        col_ind = square % 3
        column = [self.board[col_ind + 3*i] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Then, to check if the winner exists in the diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def make_move(self, square, letter):
        # if valid move, then make the move, otherwise, return false
        if self.board[square] == ' ':
            self.board[square]= letter  
            if self.winner(square, letter): # if this is true
                self.current_winner = letter
            return True
        return False

# def a function out of the TicTacToe class
def play(game, x_player, o_player, print_game=True): # print_game here means to start the game?
    if print_game:
        game.print_board_nums()   

    letter = 'X' # Lets start with 'X' 
    # iterate the game when the board still has empty squares
    while game.empty_squares(): 
        # which means its Ture
        if letter == 'O':
            square = o_player.get_move(game)   
            # here the o_player would be leveraging the funtion from player
        else:
            square = x_player.get_move(game) 
            # here the x_player would be leveraging the funtion from player

        # now we have the square which we want to move
        # and aslo has the letter
        # we need to make the move
        if game.make_move(square, letter):
            print(letter + f' makes a move to square{square}')
            game.print_board()
            print('*********')
        # here there will be no else, as typically it will return ture

        # before we switch the player, we should maker sure that there is an current winnier now
        if game.current_winner:
            if print_game:
                print(letter + ' is the winner')
                return letter

        # switch the player
        letter = 'O' if letter == 'X' else 'X' # please give a notice to the snytax
        
        time

        # now we need to consider who is the winner
    if print_game:
        print('it\'s a tie')


# start the game
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('Y')
    play(TicTacToe(), x_player, o_player, print_game=True)
    




    
