# ---------------global variable--------------
import numpy
import os

# making a game board
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


# if game is still going

game_still_going = True

# who won? or tie?
winner = None

# whos turn is it?
current_player = "X"


# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play a game of tic tac toe
def play_game():
    # display initial board
    display_board()

    # while the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game is over
        check_if_game_over()

        # flip to the other player
        flip_player()

    # the game has over

    if winner == "X" or winner == "O":
        print(winner + "  won.")

    elif winner == None:
        print("TIE")


# handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")

    position = input("Choose the position from 1 to 9:")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Please choose a position from 1 to 9:")

        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("you can't go there.Go again.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # declare winner as a gloabl variable
    global winner

    # check rows
    row_winner = check_rows()

    # check column
    column_winner = check_column()

    # check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonals_winner:
        winner = diagonals_winner

    else:
        winner = None

    return


def check_rows():

    # setup a global variable
    global game_still_going

    # check if any of the rows have same value and it should not be empty as well
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    # if any row does have a match,flag that there is a win
    if row_1 or row_2 or row_3:

        game_still_going = False

    # return the winner[ if X or O]
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


def check_column():
    # setup a global variable
    global game_still_going

    # check if any of the rows have same value and it should not be empty as well
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    # if any row does have a match,flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # return the winner[ if X or O]
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():
    # setup a global variable
    global game_still_going

    # check if any of the rows have same value and it should not be empty as well
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"

    # if any row does have a match,flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner[ if X or O]
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return


def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False

    return


def flip_player():
    # call the global variable
    global current_player
    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"
    return


play_game()
