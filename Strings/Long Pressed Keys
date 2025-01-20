a,b=input().split()
i=0
for j in range(len(b)):
    if i<len(a) and a[i]==b[j]:
        i+=1
    elif i==0 or b[j]!=b[j-1]:
        print("false")
        break
else:
    print("true" if i==len(a) else "false")
