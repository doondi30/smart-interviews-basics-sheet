n=int(input())
exp=input().split()
a=int(exp[0])
i=1
while i < len(exp):
    o = exp[i]
    if o =='+':
        a = a + int(exp[i+1])
    elif o=='-':
        a=a - int(exp[i+1])
    elif o=='*':
        a=a * int(exp[i+1])
    elif o=='/':
        a= int(a / int(exp[i+1]))
    elif o=='%':
        a=a % int(exp[i+1])
    i+=2
print(a)
