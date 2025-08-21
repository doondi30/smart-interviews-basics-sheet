a,b,c,d,e,f=map(int, input().split())
mod = int(1e9+7)

p1=(a*b*c) % mod
p2=(d*e*f) % mod

print((p1 -p2) % mod)
