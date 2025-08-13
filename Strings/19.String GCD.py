from math import gcd
p=input().strip()
q=input().strip()

if p+q != q+p:
    print(-1)
else:
    r= gcd( len(p),len(q) )
    print(p[:r])
