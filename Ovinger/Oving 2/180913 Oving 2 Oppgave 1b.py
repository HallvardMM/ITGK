#Øving 2 oppgave 1b)
epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du? "))
if barn>0:
    print("Da blir det", epler // barn, "epler til hvert barn")
    print("og", epler % barn, "epler til overs til deg selv.")
print("Takk for i dag!")
