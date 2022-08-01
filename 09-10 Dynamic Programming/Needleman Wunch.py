import numpy as np
import pandas as pd

def optimalAlignment(x, y, gap, alfa):
    nx, ny = len(x), len(y)
    if(nx == 0):
        return len(y)*gap
    if(ny == 0):
        return len(x)*gap
    p = np.full((nx+1, ny+1), 0)
    for i in range(ny+1):
        p[0, i] = i*gap
    for i in range(nx+1):
        p[i, 0] = i*gap
    
    for i in range(1, nx+1):
        for j in range(1, ny+1):
            c1 = p[i-1, j-1] + alfa[x[i-1]][y[j-1]]
            c2 = p[i-1, j] + gap
            c3 = p[i, j-1] + gap
            p[i,j] = max(c1, c2, c3)
    #print(p)
    print("Puntaje óptimo: ")
    print(p[nx,ny])
    printAlignment(p, x, y)
    return(p[nx,ny])

def printAlignment(p, x, y):
    i = len(x)
    j = len(y)
    printX = ''
    printY = ''

    while i >= 0 and j >= 0:
        if i == 0 and j == 0:
            i -= 1
            j -= 1
        elif p[i, j] < p[i-1, j]:
            printX = x[i-1] + printX
            printY = '-' + printY
            i -= 1
        elif p[i, j] < p[i, j-1]:
            printX = '-' + printX
            printY = y[j-1] + printY
            j -= 1
        else:
            printX = x[i-1] + printX
            printY = y[j-1] + printY
            i -= 1
            j -= 1
    print("Alineación Óptima:")
    print(printX)
    print(printY)


alfa = {'A': [10, -1, -3, -4],
        'G': [-1, 7, -5, -3],
        'C': [-3, -5, 9, 0],
        'T': [-4, -3, 0, 8]}
alfa2 = {'A': [1, -1, -1, -1],
        'G': [-1, 1, -1, -1],
        'C': [-1, -1, 1, -1],
        'T': [-1, -1, -1, 1]}
alfa = pd.DataFrame(alfa)
alfa = alfa.rename(index = {0:'A', 1:'G', 2:'C', 3:'T'})
gap = -5
x = "CGATGCTAGCGTATCGTAGTCTATCGTAC"
y = "ACGATGCTAGCGTTTCGTATCATCGTA"
testX = "AGGGCT"
testY = "AGGCA"
optimalAlignment(x, y, gap, alfa)