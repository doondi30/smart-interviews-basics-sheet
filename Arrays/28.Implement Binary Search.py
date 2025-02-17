a,b=map(int, input().split())
x=list(map(int, input().split()))
length=len(x)-1

low=0
high= length

while low<=high:
    mid=(low+high)//2
    print(low,high,mid)

    if x[mid]==b:
        print("True")
        break
    elif x[mid]<b:
        low= mid+1
    else:
        high =mid-1

else:
    print("False")
