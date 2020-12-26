n=int(input())
c=[1,3,4]
l=[0]
for i in range(1,n+1):
    l.append(9999999999999999999)
    for t in c:
        if i>=t:
            l[i]=min(l[i],l[i-t]+1)
print(l[n])

