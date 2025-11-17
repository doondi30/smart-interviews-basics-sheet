n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(n):
    k=n-i
    for j in range(1,k):
        print(j,end=" ")
    print()
