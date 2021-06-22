#Øving 3 oppgave 7a

while True:
    oppgave=str(input("Hvilken oppgave ønsker du (a/b/c): "))
    if oppgave=="a":
        n=int(input("n="))
        r=float(input("r="))
        x=0
        summen=0
        z=0

        while z < n+1:
            x=r**z
            summen+=x
            z+=1
        print(summen)

#Øving 3 oppgave 7b
    if oppgave=="b":
        r=float(input("r="))
        tol=float(input("tol="))
        n=0
        summen=0
        y=0
        z=1/(1 - r)

        while summen < (z-tol):
            y=r**n
            summen += y
            n += 1
        print (summen)
        print(n)
        
#Øving 3 oppgave 7c
    if oppgave=="c":
        r=float(input("r="))
        tol=float(input("tol="))
        n=0
        summen=0
        y=0
        z=1/(1 - r)

        while summen < (z-tol):
            y=r**n
            summen += y
            n += 1
        print ("For å være innenfor toleransegrensen:",tol,", kjørte løkken", n,"ganger.\nDifferansen mellom vireklig og estimert verdi var da", z-summen)
    
