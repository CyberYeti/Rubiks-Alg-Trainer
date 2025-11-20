# Efficient 3x3 cube representation using face order:
# UP, LEFT, FRONT, RIGHT, BACK, DOWN

FACE_ORDER = "ULFRBD"
COLOR_ORDER = "WOGRBY"  # White, Orange, Green, Red, Blue, Yellow

# --- 1. Build base cube ---
def solved_cube():
    """Return a solved cube in your requested face order."""
    return "".join(face * 9 for face in COLOR_ORDER)

# --- 2. Define face index groups ---
U = list(range(0, 9))
L = list(range(9, 18))
F = list(range(18, 27))
R = list(range(27, 36))
B = list(range(36, 45))
D = list(range(45, 54))

face_indices = dict(zip(FACE_ORDER, [U, L, F, R, B, D]))


# --- 3. Face rotation helpers ---
def rotate_face_clockwise(indices):
    return [
        indices[6], indices[3], indices[0],
        indices[7], indices[4], indices[1],
        indices[8], indices[5], indices[2],
    ]

def rotate_face_counter(indices):
    return [
        indices[2], indices[5], indices[8],
        indices[1], indices[4], indices[7],
        indices[0], indices[3], indices[6],
    ]

def rotate_face_180(indices):
    return [
        indices[8], indices[7], indices[6],
        indices[5], indices[4], indices[3],
        indices[2], indices[1], indices[0],
    ]


# --- 4. Define side sticker cycles for each move ---
# (Each move affects 12 stickers around its face)
face_cycles = {
    'U': [  # Top layer rotation
        11,10,9,   # L top row (reversed)
        38,37,36,  # B top row (reversed)
        29,28,27,  # R top row (reversed)
        20,19,18,  # F top row (reversed)
    ],
    'D': [  # Bottom layer rotation
        24,25,26,  # F bottom row
        33,34,35,  # R bottom row
        42,43,44,  # B bottom row
        15,16,17,  # L bottom row
    ],
    'F': [
        6,7,8,       # U bottom row
        27,30,33,    # R left column
        47,46,45,    # D top row (reversed)
        17,14,11,    # L right column (reversed)
    ],
    'B': [
        2,1,0,       # U top row (reversed)
        9,12,15,     # L left column
        51,52,53,    # D bottom row
        35,32,29,    # R right column (reversed)
    ],
    'L': [
        0,3,6,       # U left column
        18,21,24,    # F left column
        45,48,51,    # D left column
        44,41,38,    # B right column (reversed)
    ],
    'R': [
        8,5,2,       # U right column (reversed)
        36,39,42,    # B left column (reversed)
        53,50,47,    # D right column (reversed)
        26,23,20,    # F right column (reversed)
    ]
}


# --- 5. Build permutations ---
def build_permutation(face):
    indices = list(range(54))

    # Rotate the face itself
    face_pos = face_indices[face]
    new_face_pos = rotate_face_clockwise(face_pos)
    for i, j in zip(face_pos, new_face_pos):
        indices[i] = j

    # Rotate the 12 surroundimoved_backng stickers
    c = face_cycles[face]
    indices_copy = indices.copy()
    for i in range(12):
        indices[c[i]] = indices_copy[c[(i - 3) % 12]]  # shift by 3 positions

    return indices


def invert_permutation(perm):
    inverse = [0] * len(perm)
    for i, j in enumerate(perm):
        inverse[j] = i
    return inverse


def double_permutation(perm):
    twice = [0] * len(perm)
    for i in range(len(perm)):
        twice[i] = perm[perm[i]]
    return twice


# --- 6. Build all 18 move permutations ---
move_permutations = {}
for face in FACE_ORDER:
    cw = build_permutation(face)
    ccw = invert_permutation(cw)
    twice = double_permutation(cw)

    move_permutations[face] = cw
    move_permutations[face + "'"] = ccw
    move_permutations[face + "2"] = twice


# --- 7. Apply a move ---
def apply_move(state, move):
    perm = move_permutations[move]
    return ''.join(state[i] for i in perm)

def parse_moves(moves_input):
    if isinstance(moves_input, str):
        # space-separated string
        return moves_input.split()
    else:
        # already an iterable
        return list(moves_input)

def rotate_cube(state, moves):
    moves = parse_moves(moves)
    for move in moves:
        state = apply_move(state, move)
    return state

# --- 8. Test --- # check against magiccube library
if __name__ == "__main__":
    import magiccube
    from richFormatting import rich_print_colored

    # baseState = solved_cube()
    # cube = baseState
    # scramble = "F R U' L2 D B' R2 F2 U D' L B U' F'"
    # scrambled_cube = rotate_cube(cube, scramble)
    # rich_print_colored(scrambled_cube)

    # cube2 = magiccube.Cube(3, baseState) #initialize White Top Green Front
    # cube2.rotate(scramble)
    # rich_print_colored(cube2.get())

    # diff = ""
    # for i in range(54):
    #     test = scrambled_cube[i]
    #     target = cube2.get()[i]
    #     if test == target:
    #         diff += "_"
    #     else:
    #         diff += test
    #     if i % 9 == 8:
    #         diff += " "
    # rich_print_colored(diff)

    moves = [x + y for x in "L R F B D U".split() for y in ["", "2", "'"]]

    # Test 1
    magic_cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")  # initialize White Top Green Front
    for move in moves:
        test_cube = rotate_cube(solved_cube(), move)
        magic_cube.reset()
        magic_cube.rotate(move)
        assert test_cube == magic_cube.get(), f"Mismatch on move {move}"

    # Test 2
    startState = "YOGWBRGOY" * 6  # some random state
    for move in moves:
        test_cube = rotate_cube(startState, move)
        magic_cube.set(startState)
        magic_cube.rotate(move)
        assert test_cube == magic_cube.get(), f"Mismatch on move {move}"

    print("All tests passed!")
