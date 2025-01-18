from math import factorial

def isprime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input().strip())
mod=int(1e9+7)

pc=sum(1 for i in range(1,n+1) if isprime(i))   #pc prime count
npc= n-pc           #npc non prime count

r=(factorial(pc)*factorial(npc))%mod
print(r)
