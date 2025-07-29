from itertools import groupby
s=input()
print("".join(f"{char}{len(list(group))}" for char,group in groupby(s)))

# s=""
# c=1
# for i in range(1,len(n)):
#     if n[i] ==n[i-1]:
#         c+=1
#     else:
#         s+= n[i-1]+str(c)
#         c=1
# s+=n[-1]+str(c)
# print(s)
# # for i in set(n):
#     a=n.count(i)
#     print(i,a,end='',sep='')
