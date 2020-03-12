
def isInsideBoard(pos):
    return pos[0] < 8 and pos[0] >= 0 and pos[1] < 8  and pos[1] >= 0

def CanMakeMove(move, colour, board):
    if not isInsideBoard(move):
        return False
    try:
        return board[move][0] == colour
    except KeyError:
        return True

def upper_bound_moves(numTokens, pos, blackBoard=None):
    moves = []
    for step in range(1,numTokens+1):
        for dir in [(step,0),(-step,0),(0,step),(0,-step)]:
            move = (pos[0] + dir[0], pos[1] + dir[1])
            if not isInsideBoard(move):
                continue
            for amountOfTokens in range(1,numTokens+1):
                moves.append((amountOfTokens, move))
    return moves

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
def possible_moves(numTokens: int, pos: tuple, colour: str, board: dict) -> list:
    moves = []
    for step in range(1,numTokens+1):
        # List of all possible moves
        for dir in [(step,0),(-step,0),(0,step),(0,-step)]:
            move = (pos[0]+dir[0],pos[1]+dir[1])
            if(CanMakeMove(move, colour, board)):
                for amountOfTokens in range(1,numTokens+1):
                    moves.append((amountOfTokens, move))
    return moves

def MakeMove(tiles, move):
    tiles = tiles.copy()
    (numTokens, pos, to) = move
    if(tiles[pos] == numTokens):
        tiles.pop(pos)
    else:
        tiles[pos] -= numTokens
    tiles[to] = numTokens
    return tiles

def tokensToDic(tokens):
    board = {}
    for token in tokens:
        x = token[1]
        y = token[2]
        board[(x,y)] = token[0]
    return board          


