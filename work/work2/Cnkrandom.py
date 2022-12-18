import random

def rdCombined(cn, k):
    N = cn.copy()
    chooses = []
    for _ in range(k):
        i = random.randrange(0, len(N))
        chooses.append(N[i])
        del N[i]
    return chooses

N = [1,2,3,4,5]
for _ in range(10):
    print(rdCombined(N, 2))