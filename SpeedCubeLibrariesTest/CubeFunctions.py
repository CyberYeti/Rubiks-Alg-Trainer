import magiccube
from richFormatting import rich_print_colored

#Move Sequence Invertion Function
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


testSeq = "U2 R' U2 R U2 R U' R U R'"
cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY") #initialize White Top Green Front
cube.rotate(testSeq)
print("After applying moves:")
rich_print_colored(str(cube))
invertedSeq = invert_moves(testSeq)
print(f"Inverted Moves: {invertedSeq}")
cube.rotate(invertedSeq)
print("After applying inverted moves:")
rich_print_colored(str(cube))