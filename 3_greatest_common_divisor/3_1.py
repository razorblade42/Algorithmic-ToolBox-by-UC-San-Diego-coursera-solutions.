n=int(input())
ans=0
k=n//10
ans+=k
if n%10==0:
    print (k)
else:
    n %= 10
    ans += (n // 5)
    if n%5==0:
        print (ans)
    else:
        n%=5
        ans+=(n//1)
        print (ans)

