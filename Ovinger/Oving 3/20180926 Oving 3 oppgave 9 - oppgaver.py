#Øving 3 oppgave 9a
oppgave=str(input("Hvilken oppgave ønsker du (a/b): "))

while True:

    if oppgave=="a":
        n=int(input("Hvilket tall n ønsker du? "))
        summen=0
        for i in range(1,n+1):
            if i%2: 
                summen=summen-i**2
            else:
                summen=summen+i**2
        print(summen*-1)

    elif oppgave=="b": #ikke ferdig
        k=int(input("k = "))
        summen=0
        iterasjon=0
        for i in range(1,k-1):
            if(summen<k and not (i%2)):
                summen=summen+i**2
                iterasjon+=1

            elif(summen<k): 
                summen=summen-i**2
                iterasjon+=1
                
        print("Summen av tallene før summen blir større enn k er", summen*-1,". Antall itersjoner er: ",iterasjon)
