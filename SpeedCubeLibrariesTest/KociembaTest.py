import kociemba
from richFormatting import rich_print_colored
import random
import GenerateMoveSequences

#converts from ULFRBD to URFDLB
def cvt_to_kociemba(cube_str):
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

BASESTATE = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
# BASESTATE = "".join([face * 9 for face in "ULFRBD"])  # Using ULFRBD order
# KOCIEMBABASESTATE = cvt_to_kociemba(BASESTATE)

scramble = [random.choice(["L","R","F","B","D","U"]) + random.choice(["","2","'"]) for _ in range(10)]
scrambleState = GenerateMoveSequences.rotate_cube(BASESTATE, " ".join(scramble))

print(scrambleState)
solution = kociemba.solve(cvt_to_kociemba(scrambleState), cvt_to_kociemba(BASESTATE))

print(f"Scramble: {' '.join(scramble)}")
rich_print_colored(f"Scrambled Cube:\n{scrambleState}")
print(f"Kociemba Solution: {solution}")