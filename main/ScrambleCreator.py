import random
import GenerateMoveSequences
from CubeUtils import invert_moves, get_algs, kociemba_solve, rich_print_colored
from GenerateMoveSequences import rotate_cube

ollAlgs = get_algs('Algs/OCLL.json')
pllAlgs = [
    "x L2 D2 L' U' L D2 L' U L' x'",
    "x' L2 D2 L U L' D2 L U' L x",
    "R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R",
    "R2 U R' U R' U' R U' R2 U' D R' U R D'",
    "R' U' R U D' R2 U R' U R U' R U' R2 D",
    "R2 U' R U' R U R' U R2 U D' R U' R' D",
    "R U R' U' D R2 U' R U' R' U R' U R2 D'",
    "x R2 F R F' R U2 r' U r U2 x'",
    "R U R' F' R U R' U' R' F R2 U' R'",
    "R U' R' U' R U R D R' U' R D' R' U2 R'",
    "R2 F R U R U' R' F' R U2 R' U2 R",
    "R U R' U' R' F R2 U' R' U' R U R' F'",
    "x' L' U L D' L' U' L D L' U' L D' L' U L D x",
    "R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R'",
    "R' U R U' R' F' U' F R U R' F R' F' R U' R",
    "R' U R' U' y R' F' R2 U' R' U R' F R F y'",
    "F R U' R' U' R U R' F' R U R' U' R' F R F'",
    "M2 U M2 U2 M2 U M2",
    "M2 U M U2 M' U M2",
    "M2 U' M U2 M' U' M2",
    "M' U M2 U M2 U M' U2 M2"
]

def randAuf():
    return random.choice([" ", " U ", " U' ", " U2 "])

def SpecificScramble(algorithm):
    pll = random.choice(pllAlgs)
    oll = random.choice(ollAlgs)
    inverseScramble = invert_moves(randAuf() +algorithm + randAuf() + oll + randAuf() + pll + randAuf())

    BASESTATE = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
    scrambledState = GenerateMoveSequences.rotate_cube(BASESTATE, inverseScramble)

    kociembaScramble = invert_moves(kociemba_solve(scrambledState))
    return kociembaScramble#, oll, pll

if __name__ == "__main__":
    kociembaScramble = SpecificScramble("")
    print("Kociemba Scramble:")
    print(kociembaScramble)
    # print("\nOLL Algorithm:")
    # print(oll)
    # print("\nPLL Algorithm:")
    # print(pll)