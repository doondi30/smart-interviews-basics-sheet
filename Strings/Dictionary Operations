def dict():
    d={}
    n=int(input())

    for _ in range(n):
        command=input().split()
        operation,*key=command

        if operation=="insert":
            k=int(key[0])
            d[k]=d.get(k, 0)+1
            dict1(d)
        elif operation=="search":
            k=int(key[0])
            print(k in d)
        elif operation=="delete":
            k=int(key[0])
            d.pop(k,None)
            dict1(d)
        elif operation=="remove":
            k=int(key[0])
            if k in d:
                d[k]-=1
                if d[k]==0:
                    del d[k]
            dict1(d)
        elif operation=="get":
            k=int(key[0])
            print(d.get(k,0))
        elif operation=="size":
            print(len(d))

def dict1(d):
    if d:
        print(' '.join(f"{k}:{v}" for k,v in sorted(d.items())))

dict()
