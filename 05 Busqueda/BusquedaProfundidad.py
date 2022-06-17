file = open("05 Busqueda/Grafo_no_conexo.txt","r")
x = file.readlines()
v = x[1].split()

for i in range(len(v)):
    v[i] = v[i].replace('(','')
    v[i] = v[i].replace(',','')
    v[i] = v[i].replace(')','')
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

for i in range(len(e)):
    e[i] = e[i].replace('[(','')
    e[i] = e[i].replace('\n','')
    e[i] = e[i].replace(']','')
    e[i] = e[i].replace(',','')
    e[i] = e[i].replace(' (','')
    e[i] = e[i].replace(')','')
    e[i] = tuple(e[i].split(' '))

subgrafos = [1]
subgrafos[0] = [v[0]]

def busquedaProfundidad (subgrafo, e):
    
    end = False
    i = 0
    while (end == False):
        
        first = (int(e[i][0]) in subgrafo)
        second = (int(e[i][1]) in subgrafo)

        if first:
            if second:
                i = i + 1
                continue
            else:
                subgrafo.append(int(e[i][1]))
                i = 0
                continue
        elif second:
            subgrafo.append(int(e[i][0]))
            i = 0
            continue
        else:
            i = i + 1

        if i >= (len(e) - 1):
            end = True

    return subgrafo

def busquedaDFS(subgrafo, e):
    i = 1
    while (len(subgrafo) - i) >= 0:
        nuevo = busquedaDFSAux(subgrafo, e, subgrafo[len(subgrafo) - i])
        if nuevo:
            i = 1
        else:
            i = i + 1
    return subgrafo

def busquedaDFSAux(subgrafo, e, nodoActual):
    end = False
    i = 0
    nuevo = False

    while end == False:    
        first = (int(e[i][0]) == nodoActual)
        second = (int(e[i][1]) == nodoActual)

        if first:
            if (int(e[i][1]) in subgrafo):
                i = i + 1
                continue
            else:
                subgrafo.append(int(e[i][1]))
                nodoActual = int(e[i][1])
                i = 0
                nuevo = True
                continue
        elif second:
            if(int(e[i][0]) in subgrafo):
                i = i + 1
                continue
            else:
                subgrafo.append(int(e[i][0]))
                nodoActual = int(e[i][0])
                i = 0
                nuevo = True
                continue
        else:
            i = i + 1

        if i >= (len(e) - 1):
            end = True
    return nuevo

def grafosNoConexos(v = [], e = []):
    subgrafos = [1]
    subgrafos[0] = [v[0]]
    busquedaDFS(subgrafos[0], e)
    
    for i in range(len(v)):
        j = 0
        agrupado = False
        while (agrupado == False and j < len(subgrafos)):
            if v[i] in subgrafos[j]:
                agrupado = True
            else:
                j = j + 1
        if agrupado == False:
            subgrafos.append([v[i]])
            busquedaDFS(subgrafos[len(subgrafos)-1], e)

    return subgrafos

print(grafosNoConexos(v, e))


