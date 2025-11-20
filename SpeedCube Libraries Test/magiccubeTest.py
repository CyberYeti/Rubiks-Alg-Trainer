import magiccube
from richFormatting import rich_print_colored
from BruteSolver import findSolution
from CubeMoveSim import rotate_cube
import random


APERM = "x L2 D2 L' U' L D2 L' U L' x'"

scramble = [random.choice(["L","R","F","B","D","U"]) + random.choice(["","2","'"]) for _ in range(15)]
scramble = " ".join(scramble)
cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY") #initialize White Top Green Front
cube.rotate(scramble)

state = str(cube)
print(f"Scramble: {scramble}")
rich_print_colored(state)

OYBLOCK = "xxxxxxxxx xxxoooooo xxxgxxgxx xxxxxxxxx xxxxxbxxb yxxyxxyxx".upper().replace(" ", "")
scrambledOY = rotate_cube(OYBLOCK, scramble)
solutions = findSolution(scrambledOY, OYBLOCK, maxDepth=6)
if len(solutions) == 0:
    solutions = findSolution(scrambledOY, OYBLOCK, maxDepth=7)
if len(solutions) == 0:
    solutions = findSolution(scrambledOY, OYBLOCK, maxDepth=8)

print("Solutions Found:" if len(solutions) > 0 else "No Solutions Found")
for solution in solutions:
    print(solution)
