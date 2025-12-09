a,b,c=map(int, input().split())
if (a+b>c) and (b+c>a) and (c+a>b): # use AND
    print("Yes")
else:
    print("No")
