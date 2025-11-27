a,b=map(int, input().split())
c,d=1,1
for i in range(1,b+1):
    c*=(a-i+1)
    d*=i
print(c//d)
