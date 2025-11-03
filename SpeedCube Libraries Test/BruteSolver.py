from CubeMoveSim import rotate_cube

#states are expected to be in string format:
# UP, LEFT, FRONT, RIGHT, BACK, DOWN.
startState = ""
targetState = ""
startIntermediates = {}
endIntermediates = {}
possibleMoves = [x+y for x in ["U","D","L","R","F","B"] for y in ["","2","'"]]

def generateIntermediates(state: str, depth: int) -> dict[str, list[str]]:
    intermediates = {state: []}

    def backtrack(currentState: str, currentDepth: int, path: list[str]):
        if currentDepth == depth:
            return
        for move in possibleMoves:
            newState = rotate_cube(currentState, move)
            if newState not in intermediates:
                intermediates[newState] = path + [move]
                backtrack(newState, currentDepth + 1, path + [move])

    backtrack(state, 0, [])
    return intermediates

def findSolution(start: str, target: str, maxDepth: int = 6) -> list[str]:
    frontSteps = maxDepth // 2
    backSteps = maxDepth - frontSteps

    return []

    # Generate all possible intermediate states from the start state