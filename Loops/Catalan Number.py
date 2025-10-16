import math
n=int(input())

a=math.factorial(2*n)
b=math.factorial(n)
c=math.factorial(n+1)

print(a//(b*c))

'''

catalan number =      (2n)! 
                    -----------
                    (n)!(n+1)!

'''
