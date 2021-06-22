#Øving 3 oppgave 1b
print("Slå Enter uten å skrive noe når du vil avslutte.")
i = 0
while i < 1:
    adj = input("Beskriv deg selv med et adjektiv? ")
    if adj == "":
        i += 1
    else:
        print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
print("Takk for nå!")


