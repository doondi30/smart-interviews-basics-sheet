l=[]
n=int(input())

for _ in range(n):
    a=input().split()

    if a[0]=="append":
        l.append(int(a[1]))
        print(*l)
    elif a[0]=="count":
        print(l.count(int(a[1])))
    elif a[0]=="reverse":
        l.reverse()
        print(*l)
    elif a[0]=="insert":
        p=int(a[1])
        v=int(a[2])
        l.insert(p,v)
        print(*l)
    elif a[0]=="sort":
        l.sort()
        print(*l)
    elif a[0]=="index":
        v=int(a[1])
        print(l.index(v) if v in l else -1)
    elif a[0]=="length":
        print(len(l))
    elif a[0]=="extend":
        l.extend(l)
        print(*l)
