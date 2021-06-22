#Øving 3 Oppgave 4b)
#Koden gir:
#0: Dette tallet går opp i 4-gangern
#2
#4: Dette tallet går opp i 4-gangern
#6
#8: Dette tallet går opp i 4-gangern 

#Dette er fordi 0,4,8 blir 0 med mod4

for x in range(0, 10, 2):
    print(x, end='')
    if x%4==0:
        print( ": Dette tallet går opp i 4-gangern")
    else:
        print()
