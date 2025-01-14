n=int(input())
a=list(map(int, input().split()))
i=0

while i+1<n and a[i]<a[i+1]: #Ascend until peak
    i+=1

if i==0 or i==n-1: #check peak at both ends to validate 
    print("false")
else:
    while i+1<n and a[i]>a[i+1]: #descend from peak
        i+=1
    print("true" if i==n-1 else "false")
