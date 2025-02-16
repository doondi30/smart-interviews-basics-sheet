def merge(a,l,m,r):
    a[l:r+1]=sorted(a[l:r+1])
    # print(' '.join(map(str,a)))
    print(*a)
def mergesort(a,l,r):
    if l<r:
        m=(l+r)//2
        mergesort(a,l,m)
        mergesort(a,m+1,r)
        merge(a,l,m,r)

n=int(input())
a=list(map(int, input().split()))
mergesort(a,0,n-1)
