import random
import sys

def generate_test_cases(num_cases=10, starting_case=0, max_white_pieces=3, max_black_pieces=12):    
    base_name = "generated-test-"
    
    for test_no in range(starting_case, num_cases+starting_case):
        white_pieces = {}
        black_pieces = {}

        add_pieces(max_white_pieces, white_pieces)
        add_pieces(max_black_pieces, black_pieces, minimum_size = min(max_white_pieces+2, max_black_pieces))

        for piece in list(black_pieces.keys()):
            if piece in white_pieces:
                del black_pieces[piece]

        with open(base_name + str(test_no) + ".json", "w") as fname:
            print("{", file=fname)
            print("\t\"white\": [", end="", file=fname)
            for i, piece in enumerate(white_pieces):
                if i != len(white_pieces)-1:
                    print(f"[{white_pieces[piece]}, {piece[0]}, {piece[1]}], ", end="", file=fname)
                else:
                    print(f"[{white_pieces[piece]}, {piece[0]}, {piece[1]}]],", file=fname)
            print("\t\"black\": [", end="", file=fname)
            for i, piece in enumerate(black_pieces):
                if i != len(black_pieces)-1:
                    print(f"[{black_pieces[piece]}, {piece[0]}, {piece[1]}], ", end="", file=fname)
                else:
                    print(f"[{black_pieces[piece]}, {piece[0]}, {piece[1]}]]", file=fname)
            print("}", file=fname)


def generate_random_position():
    return (random.randint(0, 7), random.randint(0, 7))

def add_pieces(max_size, piece_dict: dict, minimum_size = 1):
    for j in range(random.randint(1, max_size)):
        pos = generate_random_position()
        if pos not in piece_dict:
            piece_dict[pos] = 1
        else:
            piece_dict[pos] += 1

num_cases = 8
if(len(sys.argv) >= 1):
    num_cases = int(sys.argv[1])

starting_case = 0
if(len(sys.argv) >= 2):
    starting_case = int(sys.argv[2])

print("generating ", num_cases, "starting at ", starting_case)
generate_test_cases(num_cases, starting_case)