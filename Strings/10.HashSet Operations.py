n=int(input())
a1=list(map(int, input().split()))
m=int(input())
a2=list(map(int, input().split()))

a=set(a1)
b=set(a2)

union=sorted(a|b)
print(' '.join(map(str, union)))

intersection=sorted(a&b)
if intersection:
    print(' '.join(map(str, intersection)))

symmetric=sorted(a^b)
if symmetric:
    print(' '.join(map(str, symmetric)))

print("true" if a.isdisjoint(b) else "false")
print("true" if a.issubset(b) else "false")
print("true" if a.issuperset(b) else "false")
