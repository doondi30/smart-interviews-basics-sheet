n=int(input())
x=list(map(int, input().split()))

x.sort()
# l=x[:n//2+1]
# r=x[n//2+1:]

min_diff = float('inf')
for i in range(1,n):
    diff=abs(x[i]-x[i-1])
    min_diff = min(min_diff,diff)

print(min_diff)
