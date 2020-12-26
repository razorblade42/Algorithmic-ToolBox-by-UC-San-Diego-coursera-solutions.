n = int(input())
a=[0,1]
b=[]
for i in range(2,60):
	a.append((a[i-1]+a[i-2])%10)
for t in range(60):
    b.append(sum(a[:t+1])%10)
if n<=60:
    print (b[n])
else:
    print (b[n%60])