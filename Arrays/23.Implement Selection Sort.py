n=int(input())
a=list(map(int, input().split()))

for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    a[i], a[min] = a[min],a[i]
    print(*a)
