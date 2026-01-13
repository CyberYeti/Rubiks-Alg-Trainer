import random
import GenerateMoveSequences
from CubeUtils import invert_moves, getAlgs, kociemba_solve

ollAlgs = getAlgs('Algs/CrossOLL.json')
pllAlgs = getAlgs('Algs/PLL.json')

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