import pycuber as pc
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

# --- Create and scramble cube ---
cube = pc.Cube()
moves = ["R", "U", "L", "D", "F", "B",
         "R'", "U'", "L'", "D'", "F'", "B'"]

scramble = " ".join(random.choice(moves) for _ in range(20))
cube(scramble)
print("Scramble:", scramble)

# --- Map pycuber colors to matplotlib colors ---
color_map = {
    "U": "white",    # Up
    "D": "yellow",   # Down
    "L": "orange",   # Left
    "R": "red",      # Right
    "F": "green",    # Front
    "B": "blue"      # Back
}

# --- Function to draw a single face ---
def draw_face(ax, face_matrix, start_x, start_y):
    for i, row in enumerate(face_matrix):
        for j, sticker in enumerate(row):
            color = color_map[sticker]
            # Draw square (1x1)
            rect = patches.Rectangle(
                (start_x + j, start_y - i), 1, 1,
                facecolor=color, edgecolor="black"
            )
            ax.add_patch(rect)

# --- Get cube faces as 2D arrays ---
faces = {
    "U": cube.get_face("U"),
    "L": cube.get_face("L"),
    "F": cube.get_face("F"),
    "R": cube.get_face("R"),
    "B": cube.get_face("B"),
    "D": cube.get_face("D")
}

# --- Plot cube net layout ---
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(0, 12)
ax.set_ylim(-9, 3)
ax.set_aspect("equal")
ax.axis("off")

# Place faces in a net:
#     U
#  L  F  R  B
#     D

draw_face(ax, faces["U"], 3, 0)
draw_face(ax, faces["L"], 0, -3)
draw_face(ax, faces["F"], 3, -3)
draw_face(ax, faces["R"], 6, -3)
draw_face(ax, faces["B"], 9, -3)
draw_face(ax, faces["D"], 3, -6)

plt.show()
