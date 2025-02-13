n=int(input())
x=list(map(int, input().split()))
if sum(x)%3!=0:
    print("false")
else:
    a=sum(x)//3
    b,c = 0,0
    for i in x:
        b+=i
        if b==a:
            c+=1
            b=0
        if c==3:
            print("true")
            break
    else:
        print("false")
