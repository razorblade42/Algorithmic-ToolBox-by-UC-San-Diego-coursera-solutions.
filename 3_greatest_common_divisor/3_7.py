def IsGreaterOrEqual(digit, maxDigit):
    if digit==maxDigit:
        return True
    else:
        for j in range(min(len(digit),len(maxDigit))):
            if maxDigit[j]>digit[j]:
                return False
            elif maxDigit[j]<digit[j]:
                return True
        if len(digit)>len(maxDigit):
            digit=digit[j+1:]
            return IsGreaterOrEqual(digit,maxDigit)
        else:
            maxDigit=maxDigit[j+1:]
            return IsGreaterOrEqual(digit,maxDigit)
n=int(input())
a=list(map(str,input().split()))
ans=""
while len(a)!=0:
    md=-9999999999999999999
    for d in a:
        if IsGreaterOrEqual(d,str(md)):
            md=int(d)
    ans+=str(md)
    a.remove(str(md))
print (ans)
