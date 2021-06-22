# teoritime
# Mengde (sets) er en datastruktur for å håndtere mataematiske mengder (eng:sets)
# De felste funksjoner for lister kan brukes for set
# Operasjoner for mengder de fleste som for lister

A = set([5,3,3,12])
B = set ([True, 'ost',23.2,92,False])
c = set ("aaabbcd") #gir 'a','b','c','d'
D = {2,3,5,7} # gir en mengde

for x in D:
    print(x)

if 2 in D:
    print("2 er i mengden")

# C = A.union(B) # C blir union av A og B (alle elementer i A og B)
# C = A.intersection(B) # C blir snitt av A og B
# C = A.differnece(B) # Finnes i A, men ikke i B
# C = A.symmetric_difference(B) # elementer som ikke deles av A og B
# A.issubset(B) #Sjekker om A er delmengde av B (true hvis A er i B)
# A.issuperset(B) #sjekker om A er supermengde av B (True hvis B i A)

#Oppgave



vinnertall = [1,2,3,4,5,6,7]
minetall = []
print("Skriv inn lottorekken din (Syv tall adskilt med komma).")
for i in range(7):
    unikt=False
    while not unikt:
        tall = int(input("Tall nr. " + str(i+1) + ": "))
        if tall not in minetall:
            unikt = True
            minetall.append(tall)

def sjekk_rekke(vinnertall,minetall):
    A=set(vinnertall)
    B=set(minetall)
    C= A.intersection(B)

    return len(C)

print(sjekk_rekke(vinnertall,minetall))


#Datastruktur: Dictionaries
A = {} # Tom ordbok
A['Kari']=16372138 #Oppretter et elemtent i dictionarien
tlf={'Jo':7345000, 'Per':9823123342, 'Hallvard':94155709} 
print(tlf['Hallvard']) #Skriver ut 94155709

#item(element) 'Jo':7345000
#key(indeks/nøkkel) 'Jo'
#Value(verdi) 7345000
if ('Per' in tlf):
    print(tlf['Per'])
print()


#Serialisering av objekter








