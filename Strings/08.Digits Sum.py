n=int(input())
d=n
a=0
while n>0:
    m=n%10
    a+=m
    n=n//10
print(a)
