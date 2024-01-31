"""
Tic Tac Toe Player
"""

import math
import copy

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
    # raise NotImplementedError
    #Counting all the empty spaces in the.tic tac toe.
    i=0
    for row in board:
        for column in row:
            if column == EMPTY:
                i+=1
    #If there are 9,7,5,3,1,empty spaces, then.the turn is of X.
    if i % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #Make a set named moves and put all the available ij pairs in it.
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                move = (i,j)
                moves.add(move)
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a copy of the board using deep copy.and making a new board.with it.
    new = copy.deepcopy(board)

    new[action[0]][action[1]] = player(new)

    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking all the possibilities for winning
    for i in range(3):
        if board[i][1]==board[i][0]==board[i][2]!= EMPTY:
            return board[i][1]
        elif board[0][i] == board[1][i] == board[2][i]!= EMPTY:
            return board[0][i]
    if  board[0][0] == board[1][1] == board[2][2]!= EMPTY:
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2]!= EMPTY:
        return board[1][1]

    return None





def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If the game has won or come to an end.we will return true Else faults

    for i in range(3):
        if board[i][1]==board[i][0]==board[i][2] != EMPTY:
            return True
        elif board[0][i] == board[1][i] == board[2][i]!= EMPTY:
            return True
    if  board[0][0] == board[1][1] == board[2][2]!= EMPTY:
        return True
    elif board[2][0] == board[1][1] == board[0][2]!= EMPTY:
        return True

    total=0
    for row in board:
        for column in row:
            if column == EMPTY:
                total+=1
    if total == 0:
        return True

    return False




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Implementing the Min Max function.here V is.negative infinity. at theturn of X.because X is the Max player.

    if player(board) == X:
        v = float("-inf")
        action = None
        for move in actions(board):
            minResult= minVal(result(board,move))
            if minResult > v:
                v = minResult
                action = move
    elif player(board)== O:
        v = float("inf")
        action = None
        for move in actions(board):
            maxResult= maxVal(result(board,move))
            if maxResult < v:
                v = maxResult
                action = move
    return action

def minVal(board):
    if terminal(board) == True:
        return utility(board)
    v = float("inf")
    for move in actions(board):
        v = (min(v,maxVal(result(board,move))))
    return v

def maxVal(board):
    if terminal(board) == True:
        return utility(board)
    v = float("-inf")
    for move in actions(board):
        v = (max(v,minVal(result(board,move))))
    return v