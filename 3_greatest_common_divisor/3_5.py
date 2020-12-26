n=int(input())
p=[]
for i in range(n):
    a=list(map(int,input().split()))
    p.append(a)
p=sorted(p,key=lambda x:x[1])
#print (p)
points=[]
point=p[0][1]
points.append(point)
for j in range(n):
    if point<p[j][0] or point>p[j][1]:
        point=p[j][1]
        points.append(point)
print (len(points))
for t in points:
    print (t,end=" ")
print ()
