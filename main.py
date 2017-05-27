import os
import random

def display_board(board):
    """
    Prints the tic-tac-toe board.
    """
    os.system('clear')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

board = [0, 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X']


def player_input():
    """
    Input string 'X' or 'O' and sets the marker variable equal to the input value.
    """
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    """
    Place the marker 'X' or 'O' on the board.
    """
    board[position] = marker

def win_check(board, mark):
    """
    Outputs 'True' if there is a winning line on the board.
    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def choose_first():
    """
    Randomly chooses a player to start the game (coin toss).
    """
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    """
    Returns a boolean indicating whether a space on the board is freely available.
    """
    return board[positon] == ' '

def full_board_check(board):
    """
    Checks if the board is full and returns a boolean value. True if full, false otherwise.
    """
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
