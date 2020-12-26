a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=a[0]
k=b[0]
a=a[1:]
b=b[1:]
def bs(a,x,s,e):
    if e>=s:
        m=(s+e)//2
        if a[m]==x:
            return m
        elif a[m]<x:
            s=m+1
            return bs(a,x,s,e)
        else :
            e=m-1
            return bs(a,x,s,e)
    else:
        return -1
for t in b:
    print (bs(a,t,0,n-1),end=" ")



