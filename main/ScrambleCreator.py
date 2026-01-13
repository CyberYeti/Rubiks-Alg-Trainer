import json
import random
import magiccube

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

def getAlgs(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return [alg['algorithm'] for alg in data['algs']]

ollAlgs = getAlgs('Algs/CrossOLL.json')
pllAlgs = getAlgs('Algs/PLL.json')

def SpecificScramble():
    pll = random.choice(pllAlgs)
    oll = random.choice(ollAlgs)
    inverseScramble = f"{invert_moves(pll)} {invert_moves(oll)}"

    cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY") #initialize White Top Green Front
    cube.rotate(inverseScramble)
    solver = magiccube.BasicSolver(cube)
    solution = str(solver.solve())

    kociembaScramble = invert_moves(solution.split(", "))
    return kociembaScramble, oll, pll

if __name__ == "__main__":
    kociembaScramble, oll, pll = SpecificScramble()
    print("Kociemba Scramble:")
    print(kociembaScramble)
    print("\nOLL Algorithm:")
    print(oll)
    print("\nPLL Algorithm:")
    print(pll)