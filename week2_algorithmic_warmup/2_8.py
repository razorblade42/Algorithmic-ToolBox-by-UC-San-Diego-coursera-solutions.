n = int(input())
a=[0,1]
b=[]
for i in range(2,60):
	a.append((a[i-1]+a[i-2])%10)
for x in range(60):
    a[x]*=a[x]
for t in range(60):
    b.append(sum(a[:t+1])%10)
if n<=60:
    print (b[n])
else:
    print (((n//60)*b[-1])+b[n%60])