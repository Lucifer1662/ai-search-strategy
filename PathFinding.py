
def isInsideBoard(pos):
    return pos[0] < 8 and pos[0] >= 0 and pos[1] < 8  and pos[1] >= 0

def CanMakeMove(pos, move, blackBoard):
    newPos = pos+move
    return not newPos in blackBoard and isInsideBoard(newPos) 

def AvailableActions(numTokens, pos, blackBoard):
    moves = []
    for step in range(1,numTokens+1):
        for dir in [(step,0),(-step,0),(0,step),(0,-step)]:
            if(CanMakeMove(pos, dir, blackBoard)):
                for amountOfTokens in range(1,numTokens+1):
                    moves.append((amountOfTokens, pos, pos+dir))
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


def FindPaths(tiles, targets, blackBoard):
    tokens = tokensToDic(tiles)
    for pos in tokens:
        numTokens = tokens[pos]
        for move in AvailableActions(numTokens, pos, blackBoard):
            newTokens = MakeMove(tokens, move)


