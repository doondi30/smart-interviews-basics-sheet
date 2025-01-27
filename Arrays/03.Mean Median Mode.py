n=int(input())

x=list(map(int, input().split()))
mean=sum(x)/n

# x.sort()
if n%2==0:
    median=( x[n//2] + x[(n//2)-1] ) / 2
else:
    median = x[n//2]

count=0
mode=x[0]
for i in range(n):
    c=1
    for j in range(i+1,n):
        if x[i]==x[j]:
           c+=1
    if c>count:
        count=c
        mode=x[i]

print(f"{mean:.2f} {median:.2f} {mode}")
