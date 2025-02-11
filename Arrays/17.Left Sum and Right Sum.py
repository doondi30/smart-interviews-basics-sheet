n=int(input())
a=list(map(int, input().split()))
b=[]

for i in range(n):
    l=sum(a[:i]) if i>0 else 0
    r=sum(a[i+1:]) if i< n-1 else 0
    b.append(abs(l-r))

print(" ".join(map(str, b)),end=" ")


# print(*b)
