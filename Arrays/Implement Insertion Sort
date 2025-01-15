n=int(input())
x=list(map(int, input().split()))
for i in range(1,n):
    for j in range(i,0,-1):
        if x[j] < x[j-1]:
            x[j],x[j-1] = x[j-1],x[j]
      
    print(*x)
