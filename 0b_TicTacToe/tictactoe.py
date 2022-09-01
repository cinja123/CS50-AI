"""
Tic Tac Toe Player
"""

import copy
from json.encoder import INFINITY
import math
from operator import itemgetter
from shutil import move

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    move_count = 0
    for row in board:
        move_count = move_count + row.count(X) + row.count(O)
    if move_count > 8:
        return "Game is over"
    return X if move_count % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    candidates = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                candidates.append((i, j))
    return candidates


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # Validation of action
    if board[i][j] != EMPTY:
        raise Exception("Action is not valid!")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # get diagonals
    diags = [[],[]]
    for i, rev_i in enumerate(reversed(range(len(board)))):
        diags[0].append(board[i][i])
        diags[1].append(board[rev_i][i])
    
    # check rows and columns and diagonals
    for row in board + list(zip(*reversed(board))) + diags:
        first_el = row[0]
        if first_el != EMPTY and all(cell == first_el for cell in row):
            return first_el
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # calidates if theres a winner or theres NO actions left
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    switcher = {
        X: 1,
        O: -1,
        None: 0
    }
    return switcher.get(winner(board))


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        util, action = get_optimal_action(board)
        return action


def get_optimal_action(board):
    if terminal(board):
        return utility(board), None

    # Maximizing
    if player(board) == X:
        v = -100
        act = None
        for action in actions(board):
            res_util, move = get_optimal_action(result(board, action))
            if v < res_util:
                v, act = res_util, action
                if v == 1:
                    return v, act
        return v, act
    # Minimizing
    else:
        v = 100
        act = None
        for action in actions(board):
            res_util, move = get_optimal_action(result(board, action))
            if v > res_util:
                v, act = res_util, action
                if v == -1:
                    return v, act
        return v, act