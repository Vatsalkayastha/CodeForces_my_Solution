n,k = map(int,input().split())
a=list(map(int,input().split()))
c = 0
if(n==k):
    for i in range(k):
        if(a[i]>0):
            c = c + 1 
    print(c)
else:
    for i in range(k):
        if(a[i]>0):
            c = c + 1 
    for i in range(k,n):
        if(a[i]>0 and a[i]==a[k-1]):
            c = c + 1
    print(c)
