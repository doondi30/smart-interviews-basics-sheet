n=int(input())
for i in range(1,n+1):
    left=[chr(65+j) for j in range(i)]
    right = left[:-1][::-1]
    print(' '.join(left+right))
