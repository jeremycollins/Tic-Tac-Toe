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
    return board[position] == ' '

def full_board_check(board):
    """
    Checks if the board is full and returns a boolean value. True if full, false otherwise.
    """
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    """
    Asks for a player's next position (as a number 1-9) and then uses the space_check function
    to check if it's a free position. If it is, then return the position for later use.
    """
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = input('Choose your next move: (1-9) ')
    return int(position)

def replay():
    """
    Ask the player if they want to play again. Returns a boolean True if they do want to play again.
    """
    return input('Do you want to play again? Enter Yes or No ').lower().startswith('y')




print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'Will go first')

    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations, Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations, Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
