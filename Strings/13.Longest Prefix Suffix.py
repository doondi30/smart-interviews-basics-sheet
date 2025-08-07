n=input().strip()
l=0
for i in range(1,len(n)):
    if n[:i]==n[-i:]:
        l=i
print(l)
