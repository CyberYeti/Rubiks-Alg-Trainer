from rubik.cube import Cube

def cvtLayerToFaces(input:str)->str:
    faces = ["","","","","","",""]
    for i in range(54):
        faceIndex = i // 9
        if faceIndex == 0 or faceIndex == 5:
            faces[faceIndex] += input[i]
        else:
            lineIndex = (i-9)//3
            faces[lineIndex%4+1] += input[i]
    
    return "".join(faces)

def cvtFacesToLayer(input:str)->str:
    output = ['_' for _ in range(54)]
    for i in range(54):
        faceIndex = i // 9
        if faceIndex == 0 or faceIndex == 5:
            output[i] = input[i]
        else:
            sideFaceIndex = faceIndex-1
            rowLevel = (i%9)//3
            output[9 + (rowLevel*12) + (sideFaceIndex*3) + (i%3)] = input[i]
    return "".join(output)

#A state with unique characters for testing
baseState = "qwertyuiopasdfghjklzxcvbnm12QWERTYUIOPASDFGHJKLZXCVBNM"

#generate Dict for comparisons
charDict = {}
for i, ch in enumerate(baseState):
    charDict[ch] = i

#define a function to convert state to indices
def cvtStateToIndices(state:str)->list:
    return [charDict[ch] for ch in state]

#Calculate Move Permutation
permutations = {}

#region Standard Moves
#U
cube = Cube(cvtFacesToLayer(baseState))
cube.U()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["U"] = indices
cube.U()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["U2"] = indices
cube.U()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["U'"] = indices
cube.U()

#R
cube = Cube(cvtFacesToLayer(baseState))
cube.R()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["R"] = indices
cube.R()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["R2"] = indices
cube.R()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["R'"] = indices
cube.R()

#L
cube = Cube(cvtFacesToLayer(baseState))
cube.L()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["L"] = indices
cube.L()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["L2"] = indices
cube.L()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["L'"] = indices
cube.L()

#F
cube = Cube(cvtFacesToLayer(baseState))
cube.F()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["F"] = indices
cube.F()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["F2"] = indices
cube.F()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["F'"] = indices
cube.F()

#B
cube = Cube(cvtFacesToLayer(baseState))
cube.B()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["B"] = indices
cube.B()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["B2"] = indices
cube.B()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["B'"] = indices
cube.B()

#D
cube = Cube(cvtFacesToLayer(baseState))
cube.D()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["D"] = indices
cube.D()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["D2"] = indices
cube.D()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["D'"] = indices
cube.D()
#endregion

#region Slice Moves
#S
cube = Cube(cvtFacesToLayer(baseState))
cube.S()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["S"] = indices
cube.S()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["S2"] = indices
cube.S()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["S'"] = indices
cube.S()

#E
cube = Cube(cvtFacesToLayer(baseState))
cube.E()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["E"] = indices
cube.E()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["E2"] = indices
cube.E()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["E'"] = indices
cube.E()

#M
cube = Cube(cvtFacesToLayer(baseState))
cube.M()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["M"] = indices
cube.M()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["M2"] = indices
cube.M()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["M'"] = indices
cube.M()
#endregion

#region Cube Rotations
#X
cube = Cube(cvtFacesToLayer(baseState))
cube.X()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["X"] = indices
cube.X()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["X2"] = indices
cube.X()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["X'"] = indices
cube.X()

#Y
cube = Cube(cvtFacesToLayer(baseState))
cube.Y()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["Y"] = indices
cube.Y()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["Y2"] = indices
cube.Y()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["Y'"] = indices
cube.Y()

#Z
cube = Cube(cvtFacesToLayer(baseState))
cube.Z()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["Z"] = indices
cube.Z()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["Z2"] = indices
cube.Z()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["Z'"] = indices
cube.Z()
#endregion

#region Wide Moves
# u = U + E'
cube = Cube(cvtFacesToLayer(baseState))
cube.U(); cube.Ei()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["u"] = indices
cube.U(); cube.Ei()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["u2"] = indices
cube.U(); cube.Ei()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["u'"] = indices

# d = D + E
cube = Cube(cvtFacesToLayer(baseState))
cube.D(); cube.E()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["d"] = indices
cube.D(); cube.E()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["d2"] = indices
cube.D(); cube.E()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["d'"] = indices

# l = L + M
cube = Cube(cvtFacesToLayer(baseState))
cube.L(); cube.M()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["l"] = indices
cube.L(); cube.M()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["l2"] = indices
cube.L(); cube.M()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["l'"] = indices

# r = R + M'
cube = Cube(cvtFacesToLayer(baseState))
cube.R(); cube.Mi()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["r"] = indices
cube.R(); cube.Mi()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["r2"] = indices
cube.R(); cube.Mi()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["r'"] = indices

# f = F + S
cube = Cube(cvtFacesToLayer(baseState))
cube.F(); cube.S()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["f"] = indices
cube.F(); cube.S()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["f2"] = indices
cube.F(); cube.S()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["f'"] = indices

# b = B + S'
cube = Cube(cvtFacesToLayer(baseState))
cube.B(); cube.Si()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["b"] = indices
cube.B(); cube.Si()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["b2"] = indices
cube.B(); cube.Si()
indices = cvtStateToIndices(cvtLayerToFaces("".join(str(cube).split())))
permutations["b'"] = indices
#endregion

#region Aliases
#Wide move aliases
permutations["Uw"] = permutations["u"]
permutations["Uw2"] = permutations["u2"]
permutations["Uw'"] = permutations["u'"]

permutations["Dw"] = permutations["d"]
permutations["Dw2"] = permutations["d2"]
permutations["Dw'"] = permutations["d'"]

permutations["Lw"] = permutations["l"]
permutations["Lw2"] = permutations["l2"]
permutations["Lw'"] = permutations["l'"]

permutations["Rw"] = permutations["r"]
permutations["Rw2"] = permutations["r2"]
permutations["Rw'"] = permutations["r'"]

permutations["Fw"] = permutations["f"]
permutations["Fw2"] = permutations["f2"]
permutations["Fw'"] = permutations["f'"]

permutations["Bw"] = permutations["b"]
permutations["Bw2"] = permutations["b2"]
permutations["Bw'"] = permutations["b'"]

#Cube rotation aliases
permutations["x"] = permutations["X"]
permutations["x2"] = permutations["X2"]
permutations["x'"] = permutations["X'"]

permutations["y"] = permutations["Y"]
permutations["y2"] = permutations["Y2"]
permutations["y'"] = permutations["Y'"]

permutations["z"] = permutations["Z"]
permutations["z2"] = permutations["Z2"]
permutations["z'"] = permutations["Z'"]
#endregion

def rotate_cube(state, moves):
    indicesState = [i for i in range(len(state))]
    for move in moves.split():
        perm = permutations[move]
        indicesState = [indicesState[i] for i in perm]
    finalCharState = ''.join([state[i] for i in indicesState])
    return finalCharState