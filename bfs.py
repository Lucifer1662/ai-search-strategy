import json
from util import print_board

def map_data_to_board(data: dict) -> dict:
    state = {}
    print("Data Given")
    print(data)
    for key in data:
        for i, info in enumerate(data[key]):
            state[(data[key][i][1], data[key][i][2])] = (key, data[key][i][0])

def get_piece(piece_list: list) -> tuple:
    return (piece_list[1], piece_list[2])

def is_valid_move(piece: list) -> bool:

def get_possible_moves(piece: list) -> list:
    print(piece)

