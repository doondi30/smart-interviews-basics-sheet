x,y=map(int, input().split())
p="*"*x
print(p)
for i in range(1,y-1):
    print("*"+  " "*(x-2)  +"*")
print(p)
