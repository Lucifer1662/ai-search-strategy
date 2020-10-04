from util import print_boom, print_move

def print_moves(moves):
    for move in moves:
        if(move[2] == None):
            print_boom(move[0][0], move[0][1])
        else:
            print_move(move[2],move[0][0],move[0][1],move[1][0],move[1][1])