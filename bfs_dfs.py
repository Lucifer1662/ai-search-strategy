import json
from util import print_board
from path_finding import possible_moves, isInsideBoard, all_possible_moves
from board import Board



class Node:
    def __init__(self, source, destination, numTokenTaking, parent, board: Board):
        self.source = source
        self.destination = destination
        self.numTokenTaking = numTokenTaking
        self.parent = parent
        self.board = board

    def isExplosion(self):
        return self.numTokenTaking == None

def backTrack(node: Node):
    track = []
    while(node != None):
        track.append((node.source, node.destination, node.numTokenTaking))
        node = node.parent
    track.reverse()
    return track

def nodes_from_moves(parent:Node, moves, board: Board):
    move_to_node = lambda move: Node(move[1], move[2], move[0], parent, \
        board.copy().update_board(move[1],move[2], move[0]))
    return map(move_to_node, moves)


def filter_if_not_visited(nodes, visted: set):
    newNodes = []
    for node in nodes:
        boardHash = node.board.to_hashable()
        if(not boardHash in visted):
            newNodes.append(node)
            visted.add(boardHash)
    return newNodes

def available_node_moves(parent: Node, board: Board, visted: set):
    moves = all_possible_moves(board)
    nodes = nodes_from_moves(parent, moves, board)
    return filter_if_not_visited(nodes, visted)

def can_win(board: Board):
    return True

def bfs_dfs(board: Board):
    if(not can_win(board)):
        return (False, [])
        
    visited = set()
    nodes = available_node_moves(None, board, visited)
    while(len(nodes) > 0):
        node = nodes[0]
        nodes.pop(0)
        node.board.print()
        if(node.board.no_enemies()):   
            return (True, backTrack(node))

        if(node.isExplosion()):
            (success, track) = bfs_dfs(node.board)
            if(success):
                myTrack = backTrack(node)
                myTrack.extend(track)
                return (True, myTrack)


        nodes.extend(available_node_moves(node, node.board, visited))
    return (False, [])

def bfs_dfs_depth_test(board: Board):        
    visited = set()
    nodes = available_node_moves(None, board, visited)
    for (i, node) in enumerate(nodes):
        nodes[i] = (nodes[i], 1)
    max_depth = 1
    while(len(nodes) > 0):
        (node, depth) = nodes[0]
        #print_board(node.board)
        if(depth > max_depth):
            max_depth = depth
            print("Current Max Depth:", max_depth)
        nodes.pop(0)

        temp_nodes = available_node_moves(node, node.board, visited)
        for temp_node in temp_nodes:
            nodes.append((temp_node, depth+1))
    return max_depth


def bfs_dfs_optimal(board: Board):
    if(not can_win(board)):
        return (False, [])

    visited = set()
    nodes = available_node_moves(None, board, visited)
    currentlySuccessful = False
    bestTrack = []
    while(len(nodes) > 0):
        node = nodes[0]
        nodes.pop(0)
        if(node.board.no_enemies()):   
            return (True, backTrack(node))

        if(node.isExplosion()):
            (success, track) = bfs_dfs_optimal(node.board)
            if(success):
                myTrack = backTrack(node)
                myTrack.extend(track)
                if(not currentlySuccessful):
                    bestTrack = myTrack
                currentlySuccessful = True
                if(len(bestTrack) > len(myTrack)):
                    bestTrack = myTrack


        nodes.extend(available_node_moves(node, node.board, visited))
    return (currentlySuccessful, bestTrack)
