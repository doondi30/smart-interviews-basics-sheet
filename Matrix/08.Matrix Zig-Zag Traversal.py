a,b=map(int, input().split())
x=[ list(map(int, input().split())) for _ in range(a) ]
for i in range(a):
    if i%2==0:
        print(' '.join(map(str, x[i])), end=" ")
    else:
        print(' '.join(map(str, x[i][::-1])), end=" ")
