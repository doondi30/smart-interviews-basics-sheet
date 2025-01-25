n=int(input())
x=list(map(int, input().split()))
z,p,ng=0,0,0
for i in x:
    if i<0:
        ng+=1
    elif i>0:
        p+=1
    else:
        z+=1

print(z,p,ng)
