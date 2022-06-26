import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we have not covered
        # we will save (row, col) tuples into this set
        self.dug = set() # if we dig at 0,0, then self.dug = {(0,0)} 
    
    def make_new_board(self):
        # construct a board in the list of list
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this create the the format in 
        # [[None, None ... None],
        #  [None, None ... None],
        #  [None, None ... None],
        #  ... 
        #  [None, None ... None]]

        # plant the bombs  
        # randint returns the integer both exist =
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size # we want to locate this bomb in the board 
            col = loc % self.dim_size # we want to locate this bomb in the board

            if board[row][col] == '*':
                # this means that it will encounter an existing bomb here
                continue 

            board[row][col] = '*'
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):
        # we will assign 0-8 to each empty space(without *) to represent how many neighbouring bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # we don't have to calculate anything
                    continue 
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)

    
    def get_num_neighbouring_bombs(self, row, col):
        # top_left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right:(row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # ... in total 8 neighbouring space
        # and make sure not to go out of bounds
        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1,(row+1))+1):  # remember that self.dim_size can seize the value of 10
            for c in range(max(0,col-1), min(self.dim_size-1, (col+1))+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
        
        return num_neighbouring_bombs 
    
    def dig(self, row, col):
        # dig at that location
        # return True if it is a successful dig, otherwise if bomb is dug
      
        # 1) hit a bomb, game over
        # 2) dig at the location with neighbouring bombs --> finish dig
        # 3) dig at the location without neighbouring bombs --> automatically and recursively dig neighbours
        self.dug.add((row, col)) # to keep track of the space we have dug

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # else, we have to dig recursively. the system has to walk through all neighbourings:
        for r in range(max(0, row-1), min(self.dim_size-1,(row+1))+1):  # remember that self.dim_size can seize the value of 10
            for c in range(max(0,col-1), min(self.dim_size-1, (col+1))+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
                # recurse completely
        return True  

    def __str__(self):
        # this is a magic function where if you call print on this project,
        # It will print out what this function returns

        # first, lets create a new array that what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col]) # as the self.board will return the number of bombs around
                else:
                    visible_board[row][col] = ' '

        # put this together in a string 
        string_rep = ' '
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board) #  map(lambda n: 2 * n, nums)  # print fails, so list() below <map object at 0x10ce142e8 this is why use mao
            widths.append(
            len(max(columns, key = len))   
            )
        # print the csv strings, i dont know the belowing function
        indices = [i for i in range(self.dim_size)]
        indices_row = ' '
        cells = []        
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
                

# play the game
def play(dim_size = 10, num_bombs = 10):
    # step1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # step2: show the user the board and ask for where they want to dig
    # step3a: if location is a bomb, show game over message
    # step3b: if location is not a bomb, dig automatically and recursively until each square is at least next to a bomb
    # step4: repeat steps 2 and 3a/b until there are no more square to dig --> victory
    safe = True 
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board) # just print the board 
        user_input = re.split(',(\\s)*', input('where would like to dig:'))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print('invalid input')
            continue

        # if it is valid
        safe = board.dig(row, col)
        if not safe:
            break # game over
    
    if safe:
        print('congrats')
    else:
        print('sorry,game over')
        # lets reveal the whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == '__main__':
    play()


