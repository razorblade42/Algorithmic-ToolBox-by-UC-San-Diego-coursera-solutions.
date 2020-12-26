n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
l=int(input())
c=list(map(int,input().split()))
T = [[[0 for i in range(l+1)] for j in range(m+1)]
         for k in range(n+1)]
for i in range(n + 1):
    T[i][0][0] = 0
for j in range(m + 1):
    T[0][j][0] = 0
for k in range(l + 1):
    T[0][0][k] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1,l+1):
            if a[i - 1] == b[j - 1] and b[j-1]==c[k-1]:
                T[i][j][k] = T[i-1][j-1][k-1]+1
            else:
                T[i][j][k] = max(T[i - 1][j][k] , T[i][j - 1][k],T[i][j][k-1] )
print(T[n][m][k])