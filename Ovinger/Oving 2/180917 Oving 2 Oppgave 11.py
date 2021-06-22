#Eksempel 1: imaginære løsninger
from math import sqrt
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
if b>=0:
    d1=(-b-sqrt(b**2-4*a*c))/(2*a)
    d2=(2*c)/-b-sqrt(b**2-4*a*c)
else:
    d1=(2*c)/(-b+sqrt(b**2-4*a*c))
    d2=(-b+sqrt(b**2-4*a*c))/(2*a)

d=(b**2-4*a*c)

if d<0:
    print("Andregradsligningen", float(a),"*x^2 + ", float(b),"*x + ",float(c)," har to imaginære løsninger")
elif d>0:
    print("Andregradsligningen", float(a),"*x^2 + ", float(b),"*x + ",float(c)," har to reelle løsninger ",d1," og ",d2)
else:
    print("Andregradsligningen", float(a),"*x^2 + ", float(b),"*x + ",float(c)," har en reell dobbeltrot ",((-b/(2*a))))

