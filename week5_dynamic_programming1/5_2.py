n=int(input())
l=[0]*(n+1)
for i in range(2,n+1):
    if i%2==0 and i%3!=0:
        l[i] = min(l[i//2], l[i-1])+1
    elif i%3==0 and i%2!=0:
        l[i] = min(l[i // 3], l[i - 1])+1
    elif i%2==0 and i%3==0:
        l[i] = min(l[i // 2], l[i - 1],l[i//3])+1
    elif i%2!=0 and i%3!=0:
        l[i]=l[i-1]+1
print(l[n])
#print(l)
ans=[n]
while True:
    if n==1:
        break
    elif n%2==0 and n%3!=0:
        if l[n//2]<l[n-1]:
            n=n//2
        else:
            n=n-1
        ans.append(n)
    elif n%3==0 and n%2!=0:
        if l[n//3]<l[n-1]:
            n=n//3
        else:
            n=n-1
        ans.append(n)
    elif n%6==0:
        if l[n//2]==min(l[n//2],l[n//3],l[n-1]):
            n=n//2
        elif l[n//3]==min(l[n//2],l[n//3],l[n-1]):
            n=n//3
        elif l[n-1]==min(l[n//2],l[n//3],l[n-1]):
            n=n-1
        ans.append(n)
    elif n%2!=0 and n%3!=0:
        n=n-1
        ans.append(n)
ans.reverse()
for t in ans:
    print(t,end=" ")




