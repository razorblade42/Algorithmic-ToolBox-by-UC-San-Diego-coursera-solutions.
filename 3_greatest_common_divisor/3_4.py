n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a1.sort()
a2.sort()
ans=0
for i in range(n):
    ans+=(a1[i]*a2[i])
print (ans)