#Øving 6 oppgave 3a)

#L=5
#for i in range(3)
#t=tallene i listen [1,2,3,5,7,9]
#a[i]=[5-i]
#a[5-i]=t
#returner A

#Svar Den snur listens verdi slik at output blir [9,7,5,3,2,1]

#Øving 6 oppgave 3b)

#Den returnerer listen med tallene tilfeldig.

#Øving 6 oppgave 3c)

#Den printer [7] fordi -2 og 6 begge velger verdien syv.

#øving 6 oppgave 3d)

navn = ['Carina', 'erik', 'Magnus', 'Miriam']
navn[1] = 'Erik'
print(navn)

#Den var en tuppel ikke en liste og de kan ikke enderes.

#Øving 6 oppgave 3e)

liste1 = [1,3,2,5,4,6] # Lager listen
liste1.sort() #sorterer listen fra minst til størst
liste2 = [7, 8, 9] #lager en ny liste 
liste3 = liste1+liste2 #Adderer listen slik at liste3=[1,2,3,4,5,6,7,8,9]
liste3.insert(9, 10) #Setter "10" i plass 9. som blir bakerst i listen
liste3.remove(1) #fjerner verdien "1" fra listen
liste3.reverse() #reverserer listen (speiler den)
print(liste3) #printer ut [10, 9, 8, 7, 6, 5, 4, 3, 2]




