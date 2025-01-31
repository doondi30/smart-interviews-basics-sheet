a=int(input())
b=list(map(int, input().split()))
c=int(input())
d=list(map(int, input().split()))
f=sorted(b+d)
print(' '.join(map(str, f)))


# print(*f)
