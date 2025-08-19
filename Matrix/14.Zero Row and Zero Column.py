a,b=map(int, input().split())
x=[ list(map(int, input().split())) for _ in range(a) ]
r,c=set(),set()

for i in range(a):
    for j in range(b): #identify rows cols to zero
        if x[i][j]==0:
            r.add(i)
            c.add(j)

for i in range(a):
    for j in range(b):  #update the matrix x
        if i in r or j in c:
            x[i][j]=0

for row in x:
    print(' '.join(map(str, row)))
