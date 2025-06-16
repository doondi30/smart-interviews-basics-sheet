x,y=map(int, input().split())
m=[ list(map(int, input().split())) for _ in range(x) ]
found= False

for i in range(1, x-1):
    for j in range(1,y-1):
        if m[i][j] == 1 and all(
            m[i + di][j+dj] ==0
            for di, dj in [(-1,-1),(-1,0),(-1,1),(0,-1), (0,1),(1,-1), (1,0),(1,1)]
        ):
            found=True
            break
    if found:
        break
print("Yes" if found else "No")
