#!/usr/bin/python3
import math
a,b,c=(input().split())

a=int(a);b=int(b);c=int(c)
C=int(a+b+c)
p=C/2

a=float(a);b=float(b);c=float(c)
p=float(p)
S=math.sqrt(p*(p-a)*(p-b)*(p-c))#print("%.5f"%c)

a=int(a);b=int(b);c=int(c)
cos_a=(b*b+c*c-a*a)/(2*b*c);cos_b=(c*c+a*a-b*b)/(2*c*a);cos_c=(a*a+b*b-c*c)/(2*a*b)
aca=math.acos(cos_a);acb=math.acos(cos_b);acc=math.acos(cos_c)
B=bool(1)
if(math.isclose(aca,math.pi/2,rel_tol=1e-6) or
        math.isclose(acb,math.pi/2,rel_tol=1e-6)or
        math.isclose(acc,math.pi/2,rel_tol=1e-6)):
    B=True
else:
    B=False
print("%d %.5f "%(C,S),B)