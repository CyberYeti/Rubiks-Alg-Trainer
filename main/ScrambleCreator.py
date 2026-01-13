import random
import GenerateMoveSequences
from CubeUtils import invert_moves, get_algs, kociemba_solve

ollAlgs = get_algs('Algs/OCLL.json')
pllAlgs = get_algs('Algs/PLL.json')

def SpecificScramble():
    pll = random.choice(pllAlgs)
    oll = random.choice(ollAlgs)
    inverseScramble = f"{invert_moves(pll)} {invert_moves(oll)}"

    BASESTATE = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
    scrambledState = GenerateMoveSequences.rotate_cube(BASESTATE, inverseScramble)

    kociembaScramble = invert_moves(kociemba_solve(scrambledState))
    return kociembaScramble, oll, pll

if __name__ == "__main__":
    kociembaScramble, oll, pll = SpecificScramble()
    print("Kociemba Scramble:")
    print(kociembaScramble)
    print("\nOLL Algorithm:")
    print(oll)
    print("\nPLL Algorithm:")
    print(pll)