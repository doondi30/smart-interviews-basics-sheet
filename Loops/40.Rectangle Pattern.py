n=int(input())
for i in range(n):
    for j in range(n):
        k=n-j
        print(("*" if i+j==n-1 else k),end="")
    print()
