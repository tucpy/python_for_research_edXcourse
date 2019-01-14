'''
For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3. 
Make a function create_board() that creates such a board, with values of integers 0.
Call create_board(), and store this as board.
'''

import numpy as np 
def create_board():
    return np.zeros((3,3))


'''
Use create_board() to store a board as board, 
and use place to have Player 1 place a marker on location (0, 0).
'''
def place(board, player, position):
    if player == 1 and board[position] == 0:
        board[position] = 1
    else:
        board[position] = 2
    return board

board = create_board()
place(board,1,(0,1))
place(board,2,(0,0))
'''
Create a function possibilities(board) that returns a list of all positions (tuples) 
on the board that are not occupied (0). 
(Hint: numpy.where is a handy function that returns a list of indices that meet a condition.)

'''

def possibilities_old(board):
    for x in board:
        np.where(x == 0)
        return x

print(possibilities(board))


print(board)
def possibilities(board):
    pos = []
    vt = 0
    for x in board:
        # x run from 0 to 2
        for y in range(3):
            if np.where(board == 0):
                pos.append((vt, x[y]))
                vt+=1
    return pos

print(possibilities(board))




'''
Write a function random_place(board, player) that places a marker for the current player 
at random among all the available positions (those currently set to 0).
Find possible placements with possibilities(board).
Select one possible placement at random using random.choice(selection).
board is already defined from previous exercises. 
Call random_place(board, player) to place a random marker for Player 2, 
and store this as board to update its value.

'''
import random
def random_place(board, player):
    selection = possibilities(board)
    x = random.choice(selection)
    board_update = place(board,player, x)
    return board_update

random_place(board, 2)





'''
board is already given. Call random_place(board, player) to place three pieces each 
on board for players 1 and 2.
Print board to see your result.
'''




'''
Make a function row_win(board, player) that takes the player (integer), 
and determines if any row consists of only their marker. Have it return True of this condition 
is met, and False otherwise.
board is already defined from previous exercises. Call row_win to check if Player 1 
has a complete row.
'''