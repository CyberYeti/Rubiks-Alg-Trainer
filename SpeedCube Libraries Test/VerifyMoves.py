import magiccube
from richFormatting import rich_print_colored
from GenerateMoveSequences import rotate_cube
import random


APERM = "x L2 D2 L' U' L D2 L' U L' x'"
BASESTATE = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"

scramble = [random.choice(["L","R","F","B","D","U"]) + random.choice(["","2","'"]) for _ in range(15)]
scramble = " ".join(scramble)

# scramble = "U"

def LibBaseline(start, scramble):
    cube = magiccube.Cube(3, start) #initialize White Top Green Front
    cube.rotate(scramble)
    return cube.get()

def testBaseline(start, scramble):
    return rotate_cube(start, scramble)

baseline = LibBaseline(BASESTATE, scramble)
test = testBaseline(BASESTATE, scramble)

# print(f"Scramble: {scramble}")
# rich_print_colored(f"BaseLine : {baseline}")
# rich_print_colored(f"Test     : {test}")
# print("Match" if baseline == test else "Mismatch")

# run 10000 sample tests
numTests = 10000
for _ in range(numTests):
    scramble = [random.choice(["L","R","F","B","D","U"]) + random.choice(["","2","'"]) for _ in range(15)]
    scramble = " ".join(scramble)
    baseline = LibBaseline(BASESTATE, scramble)
    test = testBaseline(BASESTATE, scramble)
    assert baseline == test, f"Mismatch on scramble {scramble}"

print (f"{numTests} tests passed!")