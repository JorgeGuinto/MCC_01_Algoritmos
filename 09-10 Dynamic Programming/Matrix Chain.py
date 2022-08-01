import numpy as np

def optMatrixProduct(p):
    n = len(p) - 1
    m = np.zeros((n,n), dtype=int)
    s = np.zeros((n,n), dtype=int)
    
    for l in range(1, n):
        for i in range(0, n-l):
            j = i + l
            m[i, j] = m[i, j-1] + (p[i]*p[j]*p[j+1])
            s[i, j] = j
            for k in range(i, j-1):
                q = m[i,k] + m[k+1, j] + p[i]*p[k+1]*p[j+1]
                if q < m[i,j]:
                    m[i,j] = q
                    s[i,j] = k + 1
    print(f"Matrix m:\n{m}")
    print(f"Matrix s:\n{s}")
    print("Chain:")
    printChain(s,1,6)
    print()
    print(f"Minimum multiplications: {m[0,len(p)-2]}")

def printChain(s,i,j):
    if i == j:
        print(f"A{i}", end = ' ')
    else:
        print("(", end = ' ')
        printChain(s,i,s[i-1, j-1])
        printChain(s,s[i-1, j-1] + 1, j)
        print(")", end = ' ')

p = [5, 10, 3, 12, 5, 50, 6]
test = [30,35,15,5,10,20,25]
optMatrixProduct(p)