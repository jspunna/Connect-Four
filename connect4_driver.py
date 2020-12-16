
#Connect Four driver

import turtle
from connect4_board import *
from connect4_game import *

RED_FILE = 'red_score.txt'
YELLOW_FILE = 'yellow_score.txt'
X_COORDINATES = [-150, -100, -50, 0, 50, 100, 150]
Y_COORDINATES = [-150, -100, -50, 0, 50, 100]

if __name__ == "__main__":
    # Make game screen
    window = turtle.Screen()
    window.setup(1000, 600)
    window.bgcolor('black')

    # Use board class to set up intial board for game
    board = Board(X_COORDINATES, Y_COORDINATES, RED_FILE, YELLOW_FILE)
    board.create_sq()
    board.create_grid()
    board.create_arrows()
    r_score = board.initialize_red_score()
    y_score = board.initialize_yellow_score()
    board.games_won_display()

    # Return a few things from Board class methods to use in the Game class
    turn = board.first_turn()
    tracker_board = board.make_tracker_board()

    # Initiate Game class
    game = Game(Y_COORDINATES, turn, tracker_board,
                r_score, y_score, RED_FILE, YELLOW_FILE)
    game.show_turn(turn)

    # Use click function to play game
    window.onclick(game.click)

