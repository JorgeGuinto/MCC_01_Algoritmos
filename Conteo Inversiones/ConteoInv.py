from operator import indexOf
file = open("03 IntegerArray.txt","r")
x = file.read().splitlines()
for i in range(len(x)):
    x[i] = int(x[i])

def sort_and_count(x):
    if len(x) == 1:
        return 0, x
    else:
        a = x[0:int(len(x)/2)]
        b = x[int(len(x)/2):len(x)]
        (ra, a) = sort_and_count(a)
        (rb, b) = sort_and_count(b)
        (rl, s) = merge_and_count(a,b)
    
    r = ra + rb + rl
    return r, s

def merge_and_count(a, b):
    count = 0
    c = []
    i = 0
    j = 0
    
    while i < len(a) and j < len(b):
        #print(type(a[0]))
        #print(type(b[0]))
        c.append(min(a[i], b[j]))
        if b[j] < a[i]:
            count += (len(a) - i)
            j += 1
        else:
            i += 1

    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])

    return count, c

(w, t) = sort_and_count(x)
print(w)
#print(t)