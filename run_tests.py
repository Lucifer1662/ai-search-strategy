import sys
import json
from os import walk
from board import Board
from bfs_dfs import bfs_dfs
import time
from multiprocessing import Process


def checkMoves(board, moves):
    for move in moves:
        board.update_board(move[0],move[1],move[2])
    return board.no_enemies()

def run_board_test(dirpath, fileName: str, printBoard = False):
    print(fileName, end=" ")
    
    with open(dirpath + "/" + fileName) as file:
        data = json.load(file)
    board = Board(data)
    if(printBoard):
        board.print()    
    (success, moves) = bfs_dfs(board)
    if(checkMoves(board, moves)):
        print("Success")
    else:
        print("Fail")

def arrayContains(list, value):
    for item in list:
        if(value == item):
            return True
    return False


def run_board_test_with_time_limit(dirpath, fileName, limit):
    
    if(not ".json" in fileName):
        return

    p = Process(target=run_board_test, args=(dirpath, fileName, "printboard" in sys.argv))
    p.start()
    seconds = 0
    while(seconds < limit and p.is_alive()):
        time.sleep(0.1)
        seconds += 0.1
    

    if(seconds == limit and p.is_alive()):
        p.terminate()
        print(fileName, " timed out after ", limit, " seconds")
    else:
        print(fileName, " took ", "%.2f" % seconds, "seconds to complete")
        print()

    


def main():
    print(sys.argv)
    for (dirpath, dirnames, filenames) in walk("./tests"):
        print(dirpath)
        print(filenames)
        for fileName in filenames:
            run_board_test_with_time_limit(dirpath, fileName, 30)



    
 
    



if __name__ == '__main__':
    main()


