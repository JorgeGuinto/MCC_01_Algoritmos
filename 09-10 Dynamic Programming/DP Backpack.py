import numpy as np

def backpack (v, w, maxC):
    V = np.zeros((len(v) + 1, maxC  + 1))
    for i in range(1, len(v) + 1):
        for x in range(0, maxC + 1):
            j = x - w[i-1]
            if j < 0:
                V[i][x] = max(V[i-1][x], 0)
            else:
                V[i][x] = max(V[i-1][x], V[i-1][j] + v[i-1])
    print(V)
    print(V[len(v)][maxC])
    findObjects(v, w, maxC, V)

def findObjects (v, w, maxC, V):
    i = len(v) + 1
    j = maxC + 1
    objects = []
    while (j > 0) and (i > 0):
        if(V[i-1][j-1] > V[i-2][j-1]):
            #Se incertó el objeto i
            objects.insert(0, [v[i-2],w[i-2]])
            j = j - w[i-2]
            i = i - 1
        else:
            i = i - 1
    print(objects)
    return objects

v2, w2 = [3, 2, 4, 4], [4, 3, 2, 3]
v = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
w = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
backpack(v, w, 140)