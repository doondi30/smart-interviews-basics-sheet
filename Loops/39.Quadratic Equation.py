a,b,c=map(int, input().split())
d = b**2 - (4*a*c)
if d>0:
    r1 =(-b +d**0.5) / (2*a)
    r2 =( -b -d**0.5) / (2*a)
    print(f"{r1:.2f} {r2:.2f}")
elif d==0:
    r =(-b)/2*a
    print(f"{r:.2f} "*2) 
else:
    print("Imaginary Roots")
