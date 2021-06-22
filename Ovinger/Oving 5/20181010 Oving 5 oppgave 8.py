#Øving 5 oppgave 8a
def toleransegrense(tol):
    prod=1
    count=0
    k=2*tol
    y=0
    prod_gammel=0
    while k>tol:
        y=y+1
        prod=prod*(1+1/(y**2))
        count=count+1
        k=prod-prod_gammel
        prod_gammel=prod
    return prod, count

tol=float(input("tol = "))

print(toleransegrense(tol))


#Gidder ikke B!
