from math import sqrt

a=float(input('nhập a: '))
b=float(input('nhập b: '))
c=float(input('nhap c: '))
delta = b*b - 4*a*c
x=-b/2*a
x1=((-b-math.sqrt(delta))/(2*a))
x2=((-b+math.sqrt(delta))/(2*a))
if a==0:
    print('pt bac 1')
elif delta<0:
    print('pt vo nghiem')
elif delta==0:
    print('pt co nghiem kep')
    print('vay x se =',x)
else:
    print('pt co 2 nghiem pb')
    print('x1= ',x1)
    print('x2= ',x2)
