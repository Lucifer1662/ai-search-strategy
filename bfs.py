import json
from util import print_board
from PathFinding import possible_moves, isInsideBoard
from explode import removeDamageTilesWithIslands

def map_data_to_board(data: dict) -> dict:
    state = {}
    for key in data:
        for i, info in enumerate(data[key]):
            state[(data[key][i][1], data[key][i][2])] = (key, data[key][i][0], False)
    return state





class Node:
    def __init__(self, pos, numTokens, parent):
        self.pos = pos
        self.numTokens = numTokens
        self.parent = parent
        self.board = {}

def backTrack(node: Node, track: list):
    track.append((node.pos, node.numTokens))
    if(node.parent):
        backTrack(node.parent, track)
    return track

def NeighborNodes(parent, moves):
    return map(lambda move: Node(move[1], move[0], parent), moves)

def getNumTokensAt(pos, numTokens, board, colour):
    tempNumTokens = numTokens
    if(pos in board and board[pos][0] == colour):
            tempNumTokens = tempNumTokens + board[pos][1]
    return tempNumTokens

def updated_board(board, source, destionation, moveN):
    board = board.copy()

    if(destionation in board):
        board[destionation] = (board[source][0], board[source][1]+moveN, board[destionation][2])
    else:
        board[destionation] = (board[source][0], moveN, False)

   
    if(board[source][1] - moveN == 0):
        board.pop(source)
    else:
        board[source] = (board[source][0], board[source][1]-moveN, board[source][2])

    return board

def move_to_update_board(pos:tuple, target:tuple, colour:str, _board: dict):
    nodes = [Node(pos, 0, None)]
    nodes[0].board = _board.copy()
    for node in nodes:
        board = node.board
        if(node.pos == target):
            track = []
            backTrack(node, track).reverse()
            return (True, track, board)

        tempNumTokens = board[node.pos][1]

        for n in NeighborNodes(node, possible_moves(tempNumTokens, node.pos, colour, board)):
            n.board = updated_board(board, node.pos, n.pos, n.numTokens)
            nodes.append(n)
    
    return (False, [], _board)

def move_to(numTokens:int, pos:tuple, target:tuple, colour:str, board: dict):
    nodes = [Node(pos, 0, None)]
    visited = set()
    for node in nodes:
        tempNumTokens = getNumTokensAt(node.pos, node.numTokens, board, colour)
        #print(tempNumTokens)
        if(node.pos == target):
            track = []
            backTrack(node, track).reverse()
            return (True, track)

        visited.add((node.pos, tempNumTokens))
        #print(possible_moves(tempNumTokens, node.pos, colour, board))
        for n in NeighborNodes(node, possible_moves(tempNumTokens, node.pos, colour, board)):
            if not (n.pos, getNumTokensAt(n.pos, n.numTokens, board, colour)) in visited:
                nodes.append(n)
    
    return (False, [])

def tokens_on_all_targets(tokens, targets):
    for target in targets:
        if not target in tokens:
            return False
    return True

def findNotFrozen(board, colour):
    for pos in board:
        if(board[pos][0] == colour and ( not board[pos][2] or board[pos][1] > 1)):
            return pos
    return None
    

def get_into_goal_state(colour, board, targets):
    if(len(targets) == 0):
        return (True, list())

    pos = findNotFrozen(board, colour)

    if(pos == None and len(targets) > 0):
        return (False, list())

    for target in targets:
        (success, moves, newBoard) = move_to_update_board(pos, target, colour, board)

        if(success):
            newTargets = removeDamageTilesWithIslands(targets[target], targets)

            newBoard[target] = (newBoard[target][0],newBoard[target][1],True)
            (success2, movess) = get_into_goal_state(colour, newBoard, newTargets)
            if(success2):
                movess.insert(0, moves)
                return (True, movess)
    return (False, [])
    
    