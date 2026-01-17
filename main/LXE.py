LXE_ALGS = ["U R U' R2 U' R U R U' R U R'", "U S R2' S' R2", "U R U' D' R U' R' U D R'", "U2 R U2 R' U R D' R U' R' D R'", "U2 R U R' U2 R D' R U' R' D R'", "U R' U' R' U R U R U R'", "R U' R' U R U R' U R' U' R U R", "U R' U' R U R U' R' U' R U R", "U' R U2 R' U R' U' R U R", "R' U' R U R U' R U' R' U R U R'", "U' R' U' R U R2 U R'", "U2 R' U2 R U2 R2 U R'", "R' U2 R' U2 R2 U' R'", "R U2 R' U R U2 R2 U' R U R", "R U' R2 U' R' U R", 'R U R2 U2 R U2 R', "R U' R2 D' R2 U R U' R2 D", "R U' R2 U' R U R2 U' R'", "U' R' D' R U R' U' D R2 U R", "U' R U' R' U R' U' R2 U R", "R U R' U' R U' R' U R' U' R U R", "U' R U2 R' U R' U' R U R2 U' R'", "U' R U R' U R' U' R U R2 U' R'", "R' U' R U R2 U' R'", "D' R' D R2 U' R2 D' R D", "U' R' U2 R U R' U' R U2 R", "U' R' U' R U R U' R U' R' U R U' R'", "U' R U R' U2 R' U' R2 U R", "U2 R' U2 R2 U2 R", "U' R D' R U' R' D R'", "S R2' S' R2 U R U' R'", "U R' U' R U' R U R U R", "U' R U2 R' U R' U' R' U R", "U R' U' R2 U R", "U' R' U' R' U' R U2 R", "U2 R U R' U' R' U' R U R", "U R' U' R U R U R U R'", "U2 S R2' S' R3 U2' R'", "U' R U R' U R' U' R' U R", "U' R U' R' U2 R' U' R2 U R", "U R' U' R U D' R U R' D R", "R' U' R2 U' R' U R U R", "U' R U2 R' U2 R' U' R2 U R", "R' D' R2 U R U' R2 D", "R' U' R' U R", 'R U2 R2 U2 R U2 R', "U' S' R U R' U R U R' S", "R U R' S R2 S' R2", "U R' U' R2 U' R' U R U' R' U R U R", "R' U' R U R U' R U R'", "R' U' R U D' R U' R' D R", "R' U2 R U2 R U2 R U R'", "U' R' U2 R U R U R", "U' R' U R U2 R2 U2 R' U' R", "U' R' U2 R' U R U R", "U' R' U' R U R", "U' R' U2 R2 U R' U R2 U' R'", "U2 R' U' R U R U2 R U R'", "U' R U' R2 U2 R U R U R", "U2 R' U' R U R2 U' R' U' R U R'", "U' R U' R2 U' R U R", "R' U2 R2 U2 R2 U' R'", "U2 R U' R' U R' U2 R U2 R2 U' R'", "R U R' S' U2 S", "U R' U' R2 U' R' U2 R2 U' R'", "U' R U2 R2 U' R U R", "U2 R' U2 R' U2 R2 U R'", "U' R U R2 U2 R U R U R", "R U R' U' S' U2 S", "U2 R' U2 R U R U' R' U R U R", "U' R U R2 U' R U R", "U2 R U R2 U' R' U R", "U R U2 R2 U' R' U R", "U' R U R U' R2 U' R2 U R2", "U2 R D' R U R' D R'", "U R' U2 R U2 R", "R' U' R U' R U2 R", "R' U2 R2 U R' U R2 U R'", "R U' R2 U' R U R U2 R U R'", "R2 U' R2 U2 R2 U R2", "R U' R' U R U' R2 U' R U R", "U' R' U' R U' R' U R2 U R", "R U' R2 U2 R U2 R2 U' R'", "R U2 R' U R' U2 R U2 R2 U' R'", "U2 R' U' R U R2 U R' U R U' R'", "R U' R' U R U2 R2 U' R U R", "R U R' U R' U' R U R2 U R'", "U2 R U R' U R' U' R2 U R", "U R U2 R' U R' U' R2 U R", "U2 R' U2 R U2 R U' R U R'", "R U' R' U R' U' R U R", "U' R U R' U R' U' R U' R U2 R", "U2 R U R2 U' R U R2 U' R'", "U R U2 R' U2 R' U2 R2 U2 R", "U R' U' R U' R U R' U' R U2 R", "U' R U' R' U R U' R' U R' U' R U R"]

# algs = []
# inp = ""
# while inp != "y":
#     inp = input("Enter algorithm (or 'y' to finish): ")
#     if inp != "y":
#         algs.append(inp)

# print (algs)

# fixed = []
# for alg in LXE_ALGS:
#     #remove parentheses
#     fixed.append(alg.replace("(", "").replace(")", ""))

# print(fixed)

# print(len(LXE_ALGS))