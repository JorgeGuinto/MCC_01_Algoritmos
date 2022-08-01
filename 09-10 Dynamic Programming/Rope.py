d = [1,2,3,4,5,6,7,8,9,10,11]
v = [1,4,10,12,15,20,21,32,31,41,51]

d2 = [1,2,3,4,5,6,7,8,9,10]
v2 = [1,5,8,9,10,17,17,20,24,30]

def maxRopeValue(d, v, n):
    r = [0]*(len(v)+1)
    s = [0]*(len(v))

    for i in range(0, n):
        q =  -2147483648
        for j in range(0, i + 1):
            x = v[j] + r[i-j]
            if (q < (v[j] + r[i-j])):
                q = v[j] + r[i-j]
                s[i] = j + 1
        r[i+1] = q
    print(f"S = {s}")
    deMaxRope(s, n-1)
    print("Valor máximo de la cuerda:")
    return r[n]

def deMaxRope(s, n):
    print("Cortes:")
    cuts = []
    while n > 0:
        cuts.append(s[n])
        n = n - s[n]
    print(cuts)

print(maxRopeValue(d, v, 11))