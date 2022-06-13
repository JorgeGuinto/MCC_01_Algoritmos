import random

def quicksort (a, min, max, randomPivot = True):
    if min < max:
        p = partition(x, min, max, randomPivot)
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

def createRandomList(n):
    a = [(i + 1) for i in range(n)]
    shuffle(a)
    return a 
 
def shuffle(a):
    for i in range(len(a)-1, 0, -1):
        j = random.randrange(i + 1)
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

print(createRandomList(5))
x = [6,8,2,5,1,4,7,3]
print(quicksort(x, 0, (len(x)-1)))