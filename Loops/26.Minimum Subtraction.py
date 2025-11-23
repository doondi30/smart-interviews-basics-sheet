n=int(input())
for i in range(n):
    if (2**i)>n:
        s=2**(i-1)
        print(n-s)
        break
