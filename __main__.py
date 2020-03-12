import sys
import json

from util import print_move, print_boom, print_board
from explode import PossibleWinningExplosions
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
    print(data)
    board = {}
    for token in data['white']:
        numOfTokens = token[0]
        x = token[1]
        y = token[2]
        board[(x,y)] = "w"

    for token in data['black']:
        numOfTokens = token[0]
        x = token[1]
        y = token[2]
        board[(x,y)] = "b"

    print_board(board, "", False, False)
    
    
    #steps
    #create graph of black nodes
    #apply 
    numOfWhite = numberOfWhite(data["white"])
    targetss = PossibleWinningExplosions(data["black"], numOfWhite)
    print(targetss)
    #for targets in targetss:
    #    (success, path) = FindPath(data["white"], targets)

    
    
            
    
    
    

def positionInBetween(pos1, pos2):
    (x1, y1) = pos1
    (x2, y2) = pos2
    return (x1 + (x1-x2)/2, y1 + (y1-y2)/2)

if __name__ == '__main__':
    main()



