x1,y1,x2,y2,x3,y3=map(int, input().split())
cp=((x2-x1)*(y3-y1))-((y2-y1)*(x3-x1))
if cp>0:
    print("LEFT")
else:
    print("RIGHT" if cp<0 else "TOUCH")

''' Line through p1,p2
vector p1 p2 = (X2-X1, Y2-Y1)
vector p1 p3 = (X3-X1, Y3-Y1)

cross product of P1P2 X P1P3= cp


'''
