import json
import magiccube

BASE_STATE = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY" # White Top, Green Front

class Cube:
    def __init__(self, base_state=BASE_STATE):
        with open("permutations.json", "r") as f:
            self.permutations = json.load(f)
            self.base_state = base_state
            self.state = self.base_state
            self.mask =  "_" * 54
            self.masked_state = self.mask_cube(self.mask)

    #region Helper Functions
    def _get_permutation(self, move):
        perm = self.permutations.get(move, None)

        if perm is None:
            raise ValueError(f"Invalid move: {move}")
        return perm
    #endregion

    #region Public Methods
    def set_base_state(self, state):
        self.base_state = state

    def reset(self):
        self.state = self.base_state

    def rotate_cube(self, state, moves):
        indicesState = [i for i in range(len(state))]
        for move in moves.split():
            perm = self._get_permutation(move)
            indicesState = [indicesState[i] for i in perm]
        finalCharState = ''.join([state[i] for i in indicesState])
        return finalCharState
    
    def mask_cube(self, mask): # '_' is no mask and any other char is masked
        # Validate mask length
        if len(mask) != 54:
            raise ValueError("Mask must be exactly 54 characters long.")
        
        # Warn user if mask colors match center colors
        center_colors = [self.state[4], self.state[13], self.state[22], self.state[31], self.state[40], self.state[49]]
        for c in mask:
            if c in center_colors:
                print(f"Warning: Mask color '{c}' matches a center color and may cause ambiguity.")
    
        #generate masked state
        masked_state = []
        for i in range(54):
            if mask[i] == '_':
                masked_state.append(self.state[i])
            else:
                masked_state.append(mask[i])
        
        self.masked_state = ''.join(masked_state)
    #endregion
    
solver = Cube()


# region Test Code
APERM = "x L2 D2 L' U' L D2 L' U L' x'"

import random
scramble = [random.choice(["L","R","F","B","D","U"]) + random.choice(["","2","'"]) for _ in range(15)]
scramble = " ".join(scramble)

def LibBaseline(start, scramble):
    cube = magiccube.Cube(3, start) #initialize White Top Green Front
    cube.rotate(scramble)
    return cube.get()

def testBaseline(start, scramble):
    return solver.rotate_cube(start, scramble)

# run 10000 sample tests
numTests = 10000
for _ in range(numTests):
    scramble = [random.choice(["L","R","F","B","D","U","M","S","E","X","Y","Z","Uw","Dw","Lw","Rw","Fw","Bw"]) + random.choice(["","2","'"]) for _ in range(15)]
    scramble = " ".join(scramble)
    baseline = LibBaseline(BASE_STATE, scramble)
    test = testBaseline(BASE_STATE, scramble)
    assert baseline == test, f"Mismatch on scramble {scramble}"
print (f"{numTests} tests passed!")

#endregion