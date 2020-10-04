from board import Board




def isInsideBoard(pos):
    return pos[0] < 8 and pos[0] >= 0 and pos[1] < 8  and pos[1] >= 0

def cane_make_move(pos: tuple, board:Board):
    return isInsideBoard(pos) and board.can_move_here(pos)

def vector_addition(tup_1: tuple, tup_2: tuple) -> tuple:
    assert(len(tup_1) == len(tup_2))
    tup = []
    for i in range(len(tup_1)):
        tup.append(tup_1[i] + tup_2[i])
    return tuple(tup)

"""
    Lists all the moves a piece of a particular colour can take given the board state

    Returns:
        List of Tuples: [(1, (2, 2)),...]
            where 1 refers to the stack size and (2, 2) refers to the position moved to
"""
def possible_moves(numTokens: int, pos: tuple, board: Board) -> list:
    moves = []
    if(numTokens>3):
        numTokens=3
    for step in range(1,numTokens+1):
        for dir in [(step,0),(-step,0),(0,step),(0,-step)]:
            move = vector_addition(pos,dir)
            if(cane_make_move(move, board)):
                for amountOfTokens in range(1,numTokens+1):
                    moves.append((amountOfTokens, pos, move))
    return moves


def all_possible_moves(board: Board):
    moves = []
    for pos in board:
        if (board.at(pos).isMyToken):
            moves.extend(possible_moves(board.at(pos).numTokens, pos, board))
            if(board.nearby_enemy(pos)):
                moves.append((None, pos, None))
    return moves
