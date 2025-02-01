n=int(input())
x=list(map(int, input().split()))
for i in range(n):
    for j in range(i+1,n):
        if x[i]==x[j]:
            print(x[i])
            break
