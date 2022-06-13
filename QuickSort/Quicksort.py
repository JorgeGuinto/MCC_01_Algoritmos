import random
import time
import matplotlib.pyplot as plt
import numpy as np

def quicksort (a, min, max, randomPivot = True):
    if min < max:
        p = partition(a, min, max, randomPivot)
        quicksort(a, min, p - 1)
        quicksort(a, p + 1, max)
    return a

def partition (a, min, max, randomPivot):
    if randomPivot:
        pivot = a[random.randrange(min, max)]
    else:
        pivot = a[max]
    
    i = min
    for j in range(min, max):
        if a[j] < pivot:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i = i + 1
    temp = a[max]
    a[max] = a[i]
    a[i] = temp
    return i

def createList(n):
    a = [(i + 1) for i in range(n)]
    return a 
 
def shuffle(a):
    for i in range(len(a)-1, 0, -1):
        j = random.randrange(i + 1)
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

#Ejercicio de experimentación -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
arreglos = [10, 100, 200, 500, 1000, 2000, 5000, 10000]
tiempos = []

for n in arreglos:
    lista = createList(n)
    tiempoEjecución = 0
    for i in range(50):
        b = lista.copy()
        shuffle(b)
        start = time.time()
        quicksort(b, 0, n-1, False)
        end = time.time()
        tiempoEjecución += end - start
    tiempos.append(tiempoEjecución/50)
    print(n)


arreglos = np.array(arreglos)
k1 = tiempos[4]/ (arreglos[4]**2)
k2 = tiempos[4] / (arreglos[4]*np.log(arreglos[4]))
plt.plot(arreglos, tiempos, label = "Quicksort")
plt.plot(arreglos, k1*arreglos**2, label = "n^2")
plt.plot(arreglos, k2*arreglos*np.log(arreglos), label = "nlogn")
plt.legend()

print(arreglos)
print(tiempos)
plt.show()