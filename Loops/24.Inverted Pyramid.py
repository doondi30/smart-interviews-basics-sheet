n=int(input())
print("* "*n)
for i in range(n-2,0,-1):
    h=(2*i)-1           #hollowspehre
    print("*"+h*" "+"*") # 5 3 1
if n>1:
    print("*")
