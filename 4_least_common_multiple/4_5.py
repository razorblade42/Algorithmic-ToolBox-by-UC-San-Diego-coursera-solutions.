s,p=map(int,input().split())
arr=[]
for i in range(s):
    a,b=map(int,input().split())
    arr.append([a,"l"])
    arr.append([b,"r"])
n=list(map(int,input().split()))
for t in n:
    arr.append([t,"p"])
arr.sort()
#print(arr)
lc=0
rc=0
s=dict()
for u in range(len(arr)):
    if arr[u][1]=="l":
        lc+=1
    elif arr[u][1]=="r":
        rc+=1
    elif arr[u][1]=="p":
        s[arr[u][0]]=abs(lc-rc)
for k in range(p):
    print(s[n[k]],end=" ")
