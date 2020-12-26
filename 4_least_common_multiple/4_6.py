c=[]
import math
n=int(input())
for _ in range(n):
    c.append(list(map(int,input().split())))
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) *
                     (p1[0] - p2[0]) +
                     (p1[1] - p2[1]) *
                     (p1[1] - p2[1]))


def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])

    return min_val
def stripClosest(strip, size, d):
    min_value=d
    strip.sort(key=lambda x:x[1])
    for i in range(size):
        j=i+1
        while j<size and dist(strip[i],strip[j])<min_value:
            min_value=dist(strip[i],strip[j])
            j+=1
    return min_value




def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)
    else:
        P.sort(key=lambda x:x[0])
        mid = n // 2
        midPoint = P[mid][0]
        dl = closestUtil(P[:mid], mid)
        dr = closestUtil(P[mid:], n - mid)
        d=min(dl,dr)
        strip=[]
        for h in range(n):
            if abs(P[h][0]-midPoint)<d:
                strip.append(P[h])
        return stripClosest(strip,len(strip),d)
print(round(closestUtil(c,n),4))