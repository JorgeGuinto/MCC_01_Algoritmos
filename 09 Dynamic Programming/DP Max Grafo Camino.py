file = open("09 Dynamic Programming\MWIS.txt","r")
#w = [5, 2, 3, 1, 18, 2, 6, 9, 12]
w = file.read().splitlines()
for i in range(len(w)):
    w[i] = int(w[i])

def maxWIS(w):
    n = len(w)
    a = [0,w[0]]
    for i in range(2, n + 1):
        a.append(max(a[i-1], a[i-2] + w[i-1]))

    i = n
    s = []
    sIndice = set()
    while (i >= 1):
        if(a[i] == a[i-1]):
            i -= 1
        else:
            s.insert(0, w[i-1])
            sIndice.add(i-1)
            i -= 2
    return s, sIndice

s, indice = maxWIS(w)
x = [1, 2, 3, 4, 17, 117, 517, 997]
for i in x:
    if i in indice:
        print(f"{i} sí está en la solución")
    else:
        print(f"{i} no está en la solución")