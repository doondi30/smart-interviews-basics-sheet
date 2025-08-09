from datetime import datetime

d=input().strip().split()
d1=datetime.strptime(d[0], "%Y-%m-%d")
d2=datetime.strptime(d[1], "%Y-%m-%d")

days=( abs(d1-d2).days )
print(days)
