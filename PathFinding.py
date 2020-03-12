
def isInsideBoard(pos):
    return pos[0] < 8 and pos[0] >= 0 and pos[1] < 8  and pos[1] >= 0

def CanMakeMove(pos, move, blackBoard):
    newPos = (pos[0]+move[0], pos[1]+move[1])
    return not newPos in blackBoard and isInsideBoard(newPos) 

def AvailableActions(numTokens, pos, blackBoard):
    moves = []
    for step in range(1,numTokens+1):
        for dir in [(step,0),(-step,0),(0,step),(0,-step)]:
            if(CanMakeMove(pos, dir, blackBoard)):
                for amountOfTokens in range(1,numTokens+1):
                    moves.append((amountOfTokens, pos, (pos[0]+dir[0],pos[1]+dir[1])))
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


    
class Node:
    def __init__(self, pos, numTokens, parent):
        self.pos = pos
        self.numTokens = numTokens
        self.parent = parent

def backTrack(node: Node, track: list):
    track.append((node.pos, node.numTokens))
    if(node.parent):
        backTrack(node.parent, track)
    return track

def NeighborNodes(parent, moves):
    return map(lambda move: Node(move[1], move[0], parent), moves)


def move_to(numTokens, pos, target, blackBoard):
    nodes = [Node(pos,numTokens, None)]
    visited = set()
    for node in nodes:
        if(node.pos == target):
            track = []
            backTrack(node, track).reverse()
            return track

        visited.add((node.pos, node.numTokens))
        for n in NeighborNodes(node, AvailableActions(node.numTokens, pos, blackBoard)):
            if not (n.pos, n.numTokens) in visited:
                nodes.append(n)
    return []

    