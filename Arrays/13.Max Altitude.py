n=int(input())
x=list(map(int, input().split()))
a=0
for i in range(n):
    a+=x[i]
    x[i]=a
print(max(x))
