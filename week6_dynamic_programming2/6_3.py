a=input()
#print(len(a))
import math
n=[]
op=[]
for i in range(len(a)):
    if i%2==0:
        n.append(int(a[i]))
    else:
        op.append(a[i])
M=[[0 for i in range(len(n))] for j in range(len(n))]
m=[[0 for i in range(len(n))] for j in range(len(n))]
def solve(a,b,o):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
def MM(i,j):
    global M,m
    mi=99999999999999
    ma=-999999999999999
    for k in range(i,j):
        x=M[i][k]
        y=m[i][k]
        x1=M[k+1][j]
        y1=m[k+1][j]
        a1=solve(x,x1,op[k])
        b1=solve(x,y1,op[k])
        c1=solve(y,x1,op[k])
        d1=solve(y,y1,op[k])
        mi=min(a1,b1,c1,d1,mi)
        ma=max(a1,b1,c1,d1,ma)
    return mi,ma
def p(n):
    global M,m
    for u in range(len(n)):
        M[u][u]=n[u]
        m[u][u]=n[u]

    for s in range(1,len(n)):
        for i in range((len(n)-s)):
            j=i+s
            m[i][j],M[i][j]=MM(i,j)
    #print(M)
    #print(m)
    return M[0][len(n)-1]
print(p(n))
