d=int(input())
m=int(input())
n=int(input())
a=list(map(int,input().split()))
a.append(d)
a.reverse()
a.append(0)
a.reverse()
def ans(a,n,m):
    r=0
    c=0
    while c<=n:
        l=c
        while c<=n and a[c+1]-a[l]<=m:
            c+=1
        if c==l:
            return -1
        if c<=n:
            r+=1
    return r

print (ans(a,n,m))

