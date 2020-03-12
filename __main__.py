import sys
import json

from util import print_move, print_boom, print_board
from explode import PossibleWinningExplosions
from PathFinding import possible_moves, isInsideBoard, upper_bound_moves
from bfs import map_data_to_board
#from PathFinding import FindPath

def numberOfWhite(tokens):
    count = 0
    for token in tokens:
        count += token[0]
    return count

def main():
    with open(sys.argv[1]) as file:
        data = json.load(file)

    # TODO: find and print winning action sequence
    print("Data", data)
    board = map_data_to_board(data)
    print("Board", board)
    for i, key in enumerate(board):
        print(f"Currently {board[key][0]} piece at {key} with k={board[key][1]}, has available actions:")
        moves = possible_moves(board[key][1], key, board[key][0], board)
        for move in moves:
            print(f"\t {move}")
        print("")

    
    Path
            
    
    
    

def positionInBetween(pos1, pos2):
    (x1, y1) = pos1
    (x2, y2) = pos2
    return (x1 + (x1-x2)/2, y1 + (y1-y2)/2)

if __name__ == '__main__':
    main()



