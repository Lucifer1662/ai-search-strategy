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


