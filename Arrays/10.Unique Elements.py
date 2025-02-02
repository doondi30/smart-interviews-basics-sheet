n=int(input())
x=list(map(int, input().split()))
for i in range(n):
    unique = True
    for j in range(n):
        if i!=j and x[i]==x[j]:
            unique = False
            break
    if unique:
        print(x[i],end=" ")
