a,b=map(int, input().split())
n=(a*b)//2  #total elements divided by 2
c=0
x=[ list(map(int, input().split())) for _ in range(a) ]
for i in range(a):
    for j in range(b):
        if x[i][j]==0:
            c+=1
print("Yes" if c>n else "No")

# if zeros are more than half of the total elements 
# then it is a sparse matrix
