import numpy as np
import random
import matplotlib.pyplot as plt

def dist (p1, p2):
    return np.sqrt(np.square(p1[0] - p2[0]) + np.square(p1[1] - p2[1])), [p1, p2]

def closestPairOfPoints (points):
    if (len(points) <= 1):
        return 0, None
    elif (len(points) == 2):
        return dist(points[0], points[1])
    elif (len(points) == 3):
        d1, p1 = dist(points[0], points[1])
        d2, p2 = dist(points[0], points[2])
        d3, p3 = dist(points[1], points[2])
        minimo = min(d1,d2,d3)
        if (minimo == d1):
            return d1, p1
        elif (minimo == d2):
            return d2, p2
        else:
            return d3, p3
    
    points.sort()
    mid = points[int(len(points)/2)]
    dl, closestPL = closestPairOfPoints(points[:int(len(points)/2)])
    dr, closestPR = closestPairOfPoints(points[int(len(points)/2):])
    if (dl < dr):
        d, closestP = dl, closestPL
    else:
        d, closestP = dr, closestPR

    s = []
    for i in points:
        if (i[0] >= (mid[0] - d) and i[0] <= (mid[0] + d)):
            s.append(i)
    for i in range(len(s)):
        for j in range(1, len(s)-i, 1):
            dc, comparison = dist(s[i], s[i+j])
            if (d > dc):
                d, closestP = dc, comparison
    return d, closestP

points = []
for i in range(30):
    points.append([random.randrange(-25, 25), random.randrange(-25,25)])

distancia, puntos = closestPairOfPoints(points)
print("Puntos generados: ")
print(points)
print(f"Los puntos más cercanos: {puntos}")
print(f"Distancia entre los puntos: {distancia}")

plt.xlim(-30, 30)
plt.ylim(-30, 30)
plt.grid()
for p in points:
    if((p[0] != puntos[0][0] or p[1] != puntos[0][1]) and (p[0] != puntos[1][0] or p[1] != puntos[1][1])):
        plt.plot(p[0], p[1], marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
plt.plot(puntos[0][0], puntos[0][1], marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")
plt.plot(puntos[1][0], puntos[1][1], marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")
plt.plot([puntos[0][0], puntos[1][0]], [puntos[0][1], puntos[1][1]], 'bo', linestyle="--", markeredgecolor="green", markerfacecolor="green")
plt.show()