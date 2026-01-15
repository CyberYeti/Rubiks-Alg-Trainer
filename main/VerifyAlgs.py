import CubeUtils

ollAlgs = CubeUtils.get_algs('Algs/OCLL.json')
pllAlgs = CubeUtils.get_algs('Algs/PLL.json')

for alg in pllAlgs:
    state = "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
    print(CubeUtils.invert_moves(alg))
    correct = input("Is this correct? (y/n): ")