import math
n=int(input())
a=[]
k=int((math.sqrt(8*n+1)-1)/2)
if not (math.sqrt(8*n+1)-1)%2:
    a=list(range(1,k+1))
else:
    a=list(range(1,k))
    a.append (int((n-((k)*(k-1)/2))))
print (len(a))
for t in a:
    print(t,end=" ")
print()

