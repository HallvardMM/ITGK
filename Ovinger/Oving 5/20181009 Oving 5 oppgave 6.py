#Øving 5 oppgave 6

a=int(input("a = "))
b=int(input("b = "))

def euklid(a,b):
    while b>0:
        b_gammel=b
        b=a%b
        a=b_gammel
    return a

def reduce_fraction(a,b):
    d=euklid(a,b)
    y=a/d
    x=b/d
    return y, x

y, x = reduce_fraction(a,b)



print("For a = ",a,"; b = ",b," skriver programmet ut", y ,"/",x)

