from operator import index
from re import template


file = open("05 Busqueda/Grafo_ponderado.txt","r")
x = file.readlines()
v = x[0].split()
v.pop(0)
for i in range(len(v)):
    v[i] = v[i].replace(',','')
    v[i] = int(v[i])

j = 0
start = False
e = []
for i in range(len(x)):
    if x[i].find('[') >= 0:
        j = i
        start = True
    if start:
        e.append(x[i])

e = list(e[0].split('), '))

for i in range(len(e)):
    e[i] = ((((e[i].replace('(','')).replace("{'weight': ",'')).replace('}','')).replace('[','')).replace(')]\n','')
    e[i] = list(e[i].split(','))
    e[i][0] = int(e[i][0])
    e[i][1] = int(e[i][1])
    e[i][2] = int(e[i][2])

def comparacion(ct, cn, ot, on, nt, nn, ruta, ruta2):
        if (ct == None):
            cn = cn + ruta[ruta2.index(on)][1]
            return cn, on, nn
        elif (cn + ruta[ruta2.index(on)][1]) > ct:
            return ct, ot, nt
        elif (cn + ruta[ruta2.index(on)][1]) < ct:
            cn = cn + ruta[ruta2.index(on)][1]
            return cn, on, nn
        else:
            return ct, ot, nt

def dijkstra(nodoInicial, nodoFinal, v, e):
    ruta = []
    ruta2 = []
    ruta.append([nodoInicial, 0, nodoInicial])
    ruta2.append(nodoInicial)

    nodoTemp = None
    costoTemp = None
    origenTemp = None
    
    while len(ruta) < len(v):
        for i in range(len(v)):
            if (v[i] in ruta2):
                continue
            else:
                for j in range(len(e)):
                    first = (e[j][0] == v[i])
                    second = (e[j][1] == v[i])
                    if first and (e[j][1] in ruta2 == False):
                        continue
                    elif second and (e[j][0] in ruta2 == False):
                        continue
                    elif first and (e[j][1] in ruta2):
                        costoTemp, origenTemp, nodoTemp = comparacion(costoTemp, e[j][2], origenTemp, e[j][1], nodoTemp, v[i], ruta, ruta2)
                    elif second and (e[j][0] in ruta2):
                        costoTemp, origenTemp, nodoTemp = comparacion(costoTemp, e[j][2], origenTemp, e[j][0], nodoTemp, v[i], ruta, ruta2)
                    else:
                        continue
                
        ruta.append([nodoTemp, costoTemp, origenTemp])
        ruta2.append(nodoTemp)
        nodoTemp = None
        costoTemp = None
        origenTemp = None
    #print(ruta)
    
    return(ruta[ruta2.index(nodoFinal)][1])

print(dijkstra(0, 14, v, e))