import random

def quicksort (a, min, max):
    if min < max:
        p = partition(x, min, max)
        quicksort(a, min, p - 1)
        quicksort(a, p + 1, max)
    return a

def partition (a, min, max):
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

x = [6,8,2,5,1,4,7,3]
print(quicksort(x, 0, (len(x)-1)))