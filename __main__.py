import sys
import json

from util import print_move, print_boom, print_board
from path_finding import possible_moves, isInsideBoard
from bfs_dfs import bfs_dfs, bfs_dfs_optimal, bfs_dfs_depth_test
from print_moves import print_moves
from board import Board

def main():
    with open(sys.argv[1]) as file:
        data = json.load(file)

    debug_bfs_dfs(data)

def debug_possible_moves(data):  
    board = Board(data)    
    print("Board", board)
    for i, key in enumerate(board):
        print(f"Currently {board[key][0]} piece at {key} with k={board[key][1]}, has available actions:")
        moves = possible_moves(board[key][1], key, board)
        for move in moves:
            print(f"\t {move}")
        print("")

def debug_bfs_dfs(data):  
    board = Board(data)    
    board.print()
    (success, moves) = bfs_dfs(board)
    print_moves(moves)

def debug_bfs_dfs_test(data):  
    board = Board(data)    
    board.print()
    max_depth = bfs_dfs_depth_test(board)
    print("Max Depth:", max_depth)

def debug_bfs_dfs_optimal(data):  
    board = Board(data)    
    board.print()
    (success, moves) = bfs_dfs_optimal(board)
    print_moves(moves)
    

def positionInBetween(pos1, pos2):
    (x1, y1) = pos1
    (x2, y2) = pos2
    return (x1 + (x1-x2)/2, y1 + (y1-y2)/2)

if __name__ == '__main__':
    main()



