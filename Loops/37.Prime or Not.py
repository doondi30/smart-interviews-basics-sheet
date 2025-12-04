n=int(input())
if n<=1:
    print("No")
elif n==2:
    print("Yes")
else:
    for i in range(2,int(n**0.5)+1): #(2,n) also fine but it 0.5 makes program execution fast
        if n%i==0:
            print("No")
            break
    else:
        print("Yes")
