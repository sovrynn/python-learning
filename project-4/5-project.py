from random import randint


EMPTY_SQUARE = 0
USER_SQUARE = 1
COMPUTER_SQUARE = 2


"""
Define a function play_game():
    Test code as you write it.
    Parameters: None
    Side Effect: Plays Tic-Tac-Toe game. Specifically, something like this:
        While there are empty squares on the board and there isn't a winner:
            Have the user select a square.
            If there's an empty square, have the computer select a square.
        Display the outcome of the game.
    Returns: None
"""
def play_game():
    board = [[EMPTY_SQUARE for _ in range(3)] for _ in range(3)]
    # Start of your code

    # End of your code


"""
Define a function exists_empty_square():
    Parameters: board
    Returns: True if there is an empty square on the board, False otherwise 
"""


"""
Define a function exists_winner():
    Parameters: board
    Returns: True if there is a winner, False otherwise
"""


"""
Define a function select_user_square():
    Parameters: board
    Side Effect: prompt the user to select a square, and mark the square as a user square on the board
    Returns: None
"""


"""
Define a function select_computer_square():
    Parameters: board
    Side Effect: randomly choose one of the empty squares and mark it as a computer square
    Returns: None
"""
def select_computer_square(board):
    empty_square_coords = []
    for row_index in range(3):
        for col_index in range(3):
            if board[row_index][col_index] == EMPTY_SQUARE:
                empty_square_coords.append([row_index, col_index])
    random_empty_square_coords = empty_square_coords[randint(0, len(empty_square_coords) - 1)]
    board[random_empty_square_coords[0]][random_empty_square_coords[1]] = COMPUTER_SQUARE


"""
Define a function display_outcome():
    Parameters: board
    Side Effect: displays the outcome of the game
    Returns: None
"""


play_game()
