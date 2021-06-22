# Tema lister og tupler 3rd edition kap 7
# Sekvenser et objekt som inneholder flere dataenheter.
# enheter som lagres i sekvens (etter hverandre). 
# en liste er mutable en tuppel er imutable

variabelnavn = [2,3,4]
print(variabelnavn)
ole_liste = ['Ole','Dole', 'Doffen']
print(ole_liste)
#En liste kan ha forskjellige datatyper
dame = ["alice",27,1550.87,True]
print(dame)
smart_liste = [1,2,3]*5
print(smart_liste)
smart_liste_tom = [None]*5
print(smart_liste_tom)
for element in dame:
    print(element, end=' ')
print()


liste = [1,3,5,7,9]*5
for element in liste:
    print(element**2, end=' ')
print()
#Indeks (posisjon) starter på null 0

indeks_liste = [2,4,6,8,10]
x = indeks_liste[0]
y = indeks_liste[4]
print(x, y)
size=len(indeks_liste)
print(size)

#Oppgave 2
lengden=len(liste)

for i in range(0,lengden,3):
    print(liste[i]**2, end=' ')
print()

# kan mutere lister
tall_liste=[1,2,3]
tall_liste[0]=3
print(tall_liste)


#Oppgave 3
tall_liste=[2,4,6,8,10,12,14,16,18,20]
x=1
for i in range(1,len(tall_liste),2):
    tall_liste[i]=3*x
    x+=1
print(tall_liste)

#Slicing (skiving) av lister kap 7.3
slice_liste = [1,2,3,4,5,6]
w=slice_liste[0:len(slice_liste):2] #[start:slutt:inkrement]
p=slice_liste[3:]
q=slice_liste[3:-1] #til men ikke med siste element
print(w)
print(p)
print(q)

#Endre liste med slice
A=[1,2,3,4,5,6]
A[:2]=[0,0]
print(A)
B=[1,2,3,4,5,6]
B[0::2]=[5,5,5]
print(B)
C=[1,2,3,4,5,6]
C[-2:]=[9,9]
print(C)
C[3:]=[]
print(C)
C[3:]=[4,5,6]
print(C)

#extend

C.extend([7,8,9])
print(C)

#append

C.append(5)
print(C)

#index
print(C.index(5))

#Operator
navneliste=['Frank','Jan','Kåre']
if 'Thomas' not in navneliste:
    print("Thomas er ikke på listen!")
    
