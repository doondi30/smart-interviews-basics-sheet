x,y=map(int, input().split())
a=[ list(map(int, input().split())) for _ in range(x) ]
b=[ list(map(int, input().split())) for _ in range(x) ]
for i in range(x):
    s=0
    for j in range(y):
        s=a[i][j]+b[i][j]
        print(s,end=" ")
    print()
