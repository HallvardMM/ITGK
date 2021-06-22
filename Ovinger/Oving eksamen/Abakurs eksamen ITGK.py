#Øving ITGK Abakus

def open_file(filename):
    with open("filename",'r') as f:
        data = f.readlines()


# Teori
# Lengste svar oftere riktig, b svar ofte riktig, Ingen eller alle er ofte riktig.
# INTOIT, Kramster, Quizlet, https://itgk.hummel.io/

# bi til hex
# 0110 0001 1010 0000 bi = 61A0
# hvis 001 1001 så er det 0001 1001

# bi til desi
# 0110 0101 = 0^7+2^6+2^5+0^4+0^3+2^2+0^1+2^0=101

# desimal til bi
# bruk metoden jeg kan fra før

# heksa til desimal
# bruk metoden du kan fra før 

#Cheatcode
# bi(0101)=de(5)=hex(5)
# bi(1010)=de(10)=hex(A)
# bi(1111)=de(15)=hex(F)

# Toerkomplement effektiv måte å representere negative tall
# eks:
# 0101 1010 <-- utgangspunkt
# 1010 0101 <-- Invertert
# 1010 0110 <-- Legg til 1
# legge på ekstra 1 ere på starten av toerkomplement vil være som å legge til 0 i starten.


# Kap 2 variabler og datatyper
# heltall, flyttall, strenger, boolean, tegn(char)

print(round(10.1451,2))#runder ikke opp på 0.5, men 0.51 
print(int(12.8)) #runder mot 0

print(ord('a')) #97 tallverdien til a
print(ord('A')) #65 tallverdien til A

print(chr(97)) # gir a som er verdien til 97


print("Hello"+"world") #ingen mellomrom
print("Hello","world") #mellomrom

# Kap 3 Betingelser og logsike uttrykk
# 0 er False alle andre verdier er True
if(-1): # mer at -1 er lov
    print("kaos")
if 1 == True: # unødeving å skrive blir True==True
    print("hei")
if not 0: #ikke false --> 0 er false
    print("heia")

variabel= "Sant" if 6>5 else "Usant"
print(variabel)

for i in range(10):
    print(i,end=' ')

##from random import randint
#random_num=0
#while not random_num==3:
#    random_num = randint(1,5)
#    print(random_num)


#continue # hopper til neste iterasjon i løkken
#break # stopper hele løkken
#return # hopper ut av løkken og funksjonen 

# lister lagrer datatyper
# element = min_liste.pop(indeks)
liste=[0,1,2,3,4,5,6]
liste.pop(4) #popper 4
liste.pop(4) #popper 5
print(liste)

tupler=('heia','dette','er','en','tuppel')

listenen=[2,1,4,3,6,5,6,5,4,3,2,1]
print(set(listenen))

dictionary={'Fornavn': ['Kåre','Jan'], 'Etternavn':"Smith"}

for keys,values in dictionary.items():
    print(keys)
    print(values)

#liste med dictionaries
liste_dict=[{'navn':'kåre'},{'navn':'kåre'}]

def elInList(element,liste):
    if element in liste:
        return True
    else:
        return False

liste=[1,2,3]
h = list(liste) #blir ikke dobbelliste
print(h)

#Kap. 8

satan=list("HEI")
satan.insert(1,"O")
print(str(satan))

y="kåre"[::-1]
print(y)

print("{} er {} år".format("Hallvard",21))

#flyttall=[1.123,2.321,3.5412]
#for element in flyttall:
#    print("Dette er et flyttall {} med to desimaler".format(str(element),.2f))

#Rekursjon

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

print(fac(5))

def fibb(n):
    if n<2:
        return n
    else:
        return fibb(n-1)+fibb(n-2)

#or

def fib(n):
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, (a+b)
    return a

def recursion(nums):
    if not nums[-1]==5:
        nums.pop()
        return recursion(nums)
    else:
        return nums

print(recursion([x for x in range(1,11)]))

# kjøretid
# bubble sort O(n^2) (while for) sorterer fra høyre mot venstre
# Insstikkssortering insertion sort O(n^2) (for while) sorterer fra venstre mot høyre
# Binærsøk O(log n) må være sortert, 

