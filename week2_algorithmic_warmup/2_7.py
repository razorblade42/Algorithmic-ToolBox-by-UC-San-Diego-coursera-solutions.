m,n = map(int,input().split())
a=[0,1]
b=[]
def getsum(n):
    for i in range(2,60):
        a.append((a[i-1]+a[i-2]))
    for t in range(60):
        b.append(sum(a[:t+1]))
    if n<=60:
        return (b[n])
    else:
        return (((n//60)*b[-1])+b[n%60])
print ((getsum(n)-getsum(m-1))%10)