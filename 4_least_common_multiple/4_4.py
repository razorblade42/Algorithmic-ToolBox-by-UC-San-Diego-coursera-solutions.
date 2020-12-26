def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergesort(L)
        mergesort(R)
        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            elif L[i]>R[j]:
                arr[k]=R[j]
                j+=1
                global o
                o+=(len(L)-i)
            else:
                arr[k] = L[i]
                i += 1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

n=int(input())
a=list(map(int,input().split()))
o=0
(mergesort(a))
print (o)