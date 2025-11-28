n=int(input())
if n<0:
    r=-int(str(-n)[::-1])
else:
    r=int(str(n)[::-1])
print(r)
