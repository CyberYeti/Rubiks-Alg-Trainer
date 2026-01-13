import json
import kociemba

def kociemba_solve(cube_state, end_state = None):

    if end_state is None:
        end_state = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
    return kociemba.solve(_cvt_to_kociemba(cube_state), _cvt_to_kociemba(end_state))

def _cvt_to_kociemba(cube_str):
    """
    Convert a 54-character cube string from ULFRBD face order
    to URFDLB (Kociemba) face order.
    """
    if len(cube_str) != 54:
        raise ValueError("Cube string must be exactly 54 characters")

    colormap = {}
    colormap[cube_str[4]] = "U"  # Center of U face
    colormap[cube_str[13]] = "L" # Center of L face
    colormap[cube_str[22]] = "F" # Center of F face
    colormap[cube_str[31]] = "R" # Center of R face
    colormap[cube_str[40]] = "B" # Center of B face
    colormap[cube_str[49]] = "D" # Center of D face
    
    kociemba_str = "".join(colormap[char] for char in cube_str)

    faces = [kociemba_str[i:i+9] for i in range(0, 54, 9)]

    # ULFRBD → URFDLB
    order = [
        0,  # U
        3,  # R
        2,  # F
        5,  # D
        1,  # L
        4   # B
    ]

    return "".join(faces[i] for i in order)

def invert_moves(sequence):
    moves = sequence

    if type(sequence) == str:
        moves = sequence.split()

    inverted = []
    for move in reversed(moves):
        if move.endswith("'"):
            inverted.append(move[:-1])
        elif move.endswith("2"):
            inverted.append(move)
        else:
            inverted.append(move + "'")

    if type(sequence) == str:
        inverted = " ".join(inverted)

    return inverted

def get_algs(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return [alg['algorithm'] for alg in data['algs']]