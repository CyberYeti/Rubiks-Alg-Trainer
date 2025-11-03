import magiccube
from richFormatting import rich_print_colored

scramble = "x L2 D2 L' U' L D2 L' U L' x'"

cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY") #initialize White Top Green Front
cube.rotate(scramble)

state = str(cube)
rich_print_colored(state)