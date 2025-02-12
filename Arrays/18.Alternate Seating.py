n=int(input())
m=int(input())
arr=list(map(int, input().split()))
count=0
ans="NO"

for i in range(m):
    if arr[i]==0 and (i==0 or arr[i-1]==0) and (i==m-1 or arr[i+1]==0):
        count+=1
        arr[i]=1
    if count>=n:
        ans="YES"
        break
print(ans)
