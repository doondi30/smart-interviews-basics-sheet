s=input().strip()
n=len(s)
m=0

lower= any(c.islower() for c in s) 
upper= any(c.isupper() for c in s)
digit= any(c.isdigit() for c in s)
spl= any(c in "!@#$%^&*()-+" for c in s)

if not lower:
    m+=1
if not upper:
    m+=1
if not digit:
    m+=1
if not spl:
    m+=1

m=max(m,6-n)

print(m)
