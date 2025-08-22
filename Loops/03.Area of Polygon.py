n=int(input())
v= [ tuple(map(int, input().split())) for _ in range(n) ]
v.append(v[0])  #added 1st vertex v to end, 
a=0             #else RUN TIME ERROR index out of range

for i in range(n):
    x1,y1 =v[i]
    x2,y2 =v[i+1]
    a+=(x1*y2)-(y1*x2)

print(abs(a))
