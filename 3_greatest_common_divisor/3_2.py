n,w=map(int,input().split())
a=dict()
v=dict()
h=[]
tb=0
tk=0
for i in range(n):
    k,b=map(int,input().split())
    tk+=k
    tb+=b
    a[k/b]=b
    v[k/b]=k
h=list(a)
h=sorted(h,reverse=True)
#print (a)
#print(h)
if w>tb:
    print (tk)
else:
    i=0
    value=0
    while w>=0:
        if w==0:
            print(round(value,4))
            break
        else:
            value+=(min(w,a[h[i]])*(h[i]))
            w -= min(w, a[h[i]])
        i+=1



