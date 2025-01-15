n=int(input())
a=list(map(int, input().split()))

gap =n//2

while gap>0:
    for i in range(gap,n):
        temp,j=a[i],i
        while j>= gap and a[j- gap] > temp:
            a[j] = a[j - gap]
            j-= gap
        a[j]=temp
    print(*a)
    gap//=2
