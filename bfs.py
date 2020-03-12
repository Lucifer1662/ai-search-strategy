import json
from util import print_board
from PathFinding import possible_moves, isInsideBoard

def map_data_to_board(data: dict) -> dict:
    state = {}
    print("Data Given")
    print(data)
    for key in data:
        for i, info in enumerate(data[key]):
            state[(data[key][i][1], data[key][i][2])] = (key, data[key][i][0])
    print(type(state))
    return state





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

def move_to(numTokens:int, pos:tuple, target:tuple, colour:str, board: dict):
    nodes = [Node(pos,numTokens, None)]
    visited = set()
    for node in nodes:
        if(node.pos == target):
            track = []
            backTrack(node, track).reverse()
            return (True, track)

        visited.add((node.pos, node.numTokens))
        for n in NeighborNodes(node, possible_moves(node.numTokens, pos, colour,  board)):
            if not (n.pos, n.numTokens) in visited:
                nodes.append(n)
    return (False, [])

    