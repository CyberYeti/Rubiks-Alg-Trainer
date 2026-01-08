import pycuber as pc
import random

# Create a solved cube
cube = pc.Cube()
print("Solved cube:")
print(cube)

# Define a small set of moves
moves = ["R", "U", "L", "D", "F", "B",
         "R'", "U'", "L'", "D'", "F'", "B'"]

# Create a random scramble of 20 moves
scramble = [random.choice(moves) for _ in range(20)]
scramble_seq = " ".join(scramble)
print("\nScramble sequence:", scramble_seq)

# Apply scramble to the cube
cube(scramble_seq)
print("\nScrambled cube:")
print(cube)

# Apply some example moves (e.g., solve cross step)
example_moves = "R U R' U'"
cube(example_moves)
print("\nAfter applying R U R' U':")
print(cube)
