n=int(input())
for i in range(1,n+1):
    print("*"*i,end=" ")
    print()
for j in range(1,n):
    k=n-j
    print("*"*k,end=" ")
    print()
