
def getperiod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return i + 1
def getfb(n):
    a=[0,1]
    for i in range(2, n + 1):
        a.append((a[i - 1] + a[i - 2])%m)
    return a[n]
n, m = map(int, input().split())
k=n%getperiod(m)
print (getfb(k)%m)
