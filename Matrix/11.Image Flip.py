a,b= map(int, input().split())
x=[ list(map(int, input().split())) for _ in range(a) ]

for i in range(a):
    x[i]=x[i][::-1]     #reversing row order

for i in range(a):
    for j in range(b):              # 1- '0' = 1      1- '1' = 0
        x[i][j] = 1 - x[i][j]         #swapping 0 and 1 

for i in range(a):
    for j in range(b):
        print(x[i][j],end=" ")      #result data
    print()
