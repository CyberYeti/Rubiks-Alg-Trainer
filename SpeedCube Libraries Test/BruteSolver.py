from CubeMoveSim import rotate_cube

#states are expected to be in string format:
# UP, LEFT, FRONT, RIGHT, BACK, DOWN.
possibleMoves = [x+y for x in ["U","D","L","R","F","B"] for y in ["","2","'"]]

def generateIntermediates(state: str, depth: int) -> dict[str, str]:
    intermediates = {}
    intermediates[state] = ""
    currentLevel = [state]
    nextLevel = []

    for _ in range(depth):
        for cubeState in currentLevel:
            for move in possibleMoves:
                newState = rotate_cube(cubeState, move)
                if newState not in intermediates:
                    intermediates[newState] = intermediates[cubeState] + move + " "
                    nextLevel.append(newState)
        currentLevel = nextLevel
        nextLevel = []

    return intermediates

def invertMove(move: str) -> str:
    if move.endswith("'"):
        return move[:-1]
    elif move.endswith("2"):
        return move
    else:
        return move + "'"

def findSolution(start: str, target: str, maxDepth: int = 6) -> set[str]:
    startState = start.replace(" ", "")
    targetState = target.replace(" ", "")
    
    if len(startState) != 54 or len(targetState) != 54:
        raise ValueError("Invalid cube state length. Expected 54 characters.")

    frontSteps = maxDepth // 2
    backSteps = maxDepth - frontSteps

    frontIntermediates = generateIntermediates(startState, frontSteps)
    backIntermediates = generateIntermediates(targetState, backSteps)

    solutions = set()
    for state in frontIntermediates:
        if state in backIntermediates:
            frontMoves = frontIntermediates[state].strip().split(" ")
            backMoves = backIntermediates[state].strip().split(" ")
            backMoves = [invertMove(m) for m in reversed(backMoves)]
            solutions.add(" ".join(frontMoves + backMoves))

    return solutions

    # Generate all possible intermediate states from the start state

OYBLOCK = "xxxxxxxxx xxxoooooo xxxgxxgxx xxxxxxxxx xxxxxbxxb yxxyxxyxx".upper()
cur = "xxOxxxxGx xxxxOxxxx xOxxxYxxO xxBOxxGBx Yxxxxxxxx xxYxxOxxx".upper()

if __name__ == "__main__":
    import magiccube
    from richFormatting import rich_print_colored
    startState = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
    cube = magiccube.Cube(3, OYBLOCK.replace("X","W"))
    print("Target State:")
    rich_print_colored(str(cube))

    cube = magiccube.Cube(3, cur.replace("X","W"))
    print("Current State:")
    rich_print_colored(str(cube))

    print(findSolution(cur, OYBLOCK, maxDepth=12))