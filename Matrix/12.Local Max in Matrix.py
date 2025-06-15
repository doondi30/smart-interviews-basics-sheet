n=int(input())
m=[ list(map(int, input().split())) for _ in range(n) ]

for i in range(1,n-1):
    for j in range(1,n-1):
        matrix= max(m[i-1][j-1],m[i-1][j],m[i-1][j+1],
        m[i][j-1],m[i][j],m[i][j+1],m[i+1][j-1],m[i+1][j],m[i+1][j+1])
        print(matrix,end=' ')
    print()
