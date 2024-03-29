a=float(input('moi ban nhap a: '))
b=float(input('moi ban nhap b: '))
c=float(input('moi ban nhap c: ')) 
delta= b*b - 4*a*c
if delta < 0: print('phuong trinh vo nghiem')
elif delta==0:
    print('phuong trinh co nghiem kep x1=x2=',-b/(2*a))
else:
    import math
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=-b/a -x1
    print('phuong trinh co nghiem phan biet')
    print('x1= ',x1,'x2=',x2)