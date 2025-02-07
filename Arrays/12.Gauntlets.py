n=int(input())
c=0
x=list(map(int, input().split()))
# for i in range(n):

#     for j in range(n):
#         if i!=j and x[i]==x[j]:
#             c+=1
#             break

# print(c//2)

for i in set(x):
    c+=x.count(i)//2
print(c)
