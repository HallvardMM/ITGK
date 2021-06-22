#Øving 2 oppgave 7a
dager=int(input("Dager til du skal reise? "))
if dager>=14:
    print("Du kan få minipris: 199,-")
    
else:
    print("For sent for minipris; fullpris 440,-")

#Øving 2 oppgave 7b
dager=int(input("Dager til du skal reise? "))
if dager>=14:
    print("Minipris 199,- kan ikke refunderes/endres")
    minipris=str(input("Ønskes dette (J/N)? "))
    if minipris=="J":
        print("Takk for pengene, god reise!")
    else:
        alder=int(input("Skriv inn din alder: "))
        if alder<16:
            print("Prisen på biletten blir: 220,-")
        else:
            senior=str(input("Er du senior, militær eller student (J/N)? "))
            if senior=="J":
                print("Prisen på biletten blir: 330,-")
            else:
                print("Da tilbyr vi fullpris: 440,-")
else:
    alder=int(input("Skriv inn din alder: "))
    if alder<16:
        print("Prisen på biletten blir: 220,-")
    else:
        senior=str(input("Er du senior, militær eller student (J/N)? "))
        if senior=="J":
            print("Prisen på biletten blir: 330,-")
        else:
            print("Da tilbyr vi fullpris: 440,-")

