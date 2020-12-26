W,n=map(int,input().split())
a=list(map(int,input().split()))
b=[[0]*(W+1)]
l=b*(n+1)
val=0
for i in range(1,n+1):
    for j in range(1,W+1):
        l[i][j] = l[i - 1][j]
        if (a[i - 1] <= j):
            val = l[i-1][j - a[i-1]] + a[i-1]
            if (l[i][j] < val) :
                l[i][j] = val
print(l)
