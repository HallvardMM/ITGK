# Kræsjkurs i python med Tekna 
# teori memorizer.io

# Datatyper: int,float,boolean,strings

datatyper=['int', 'float','boolean','strings']
for element in datatyper:
    print(element)

print(str(float(int(12))))

#if-elif-else
for i in range(5):
    print('Hallo jeg er kul',end=' ')
print()

def isTure(ting):
    if ting==True:
        return True
    else:
        return False

def to_tall(x,y):
    if x>y:
        return x
    else:
        return y

def kvadrat(x):
    return x**2

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(5)) #iterative funksjoner er raskere enn rekursive

for n in range(5):
    string=str(n)
    print(string)


#eksamen oppgave 2012

def summerOlympics(firstyear,lastyear):
    liste=[]
    for i in range(firstyear,lastyear+1):
        if i%4==0:
            liste.append(i)
    return liste

print(summerOlympics(1999,2016))

#Highscore

def check_highscore(points,scores):
    for place in scores:
        if points>scores[place][1]:
            return place
    return -1
 
def print_highscores(scores):
    for x in scores:
        print(str(x).rjust(2)+" "+scores[x][0].ljust(20)+str(scores[x][1]).rjust(5))
 
def add_highscore(points,name,scores):
    place = check_highscore(points,scores)
    print(place)
    if not place==-1:
        changes = len(scores)-place
        for i in range(changes):
            scores[len(scores)-i] = scores[len(scores)-1-i]
        scores[place] = [name,points]
    return scores
 
 
highscores = {}
highscores[1] = ['Vernon',100]
highscores[2] = ['Sirius',90]
highscores[3] = ['Severus',80]
highscores= add_highscore(50,"hei",highscores)
print_highscores(highscores)

#Konsertsystem

def payment(pris, antall):
    if antall > 3:
        return 0.9*antall*pris
    else:
        return antall*pris
 
def get_price(konsert):
    fil = open('prices.txt')
    linjer = fil.readlines()
    for i in range(len(linjer)):
        linjer[i]=linjer[i].split(';')
    for i in linjer:
        if i[0]== konsert:
            fil.close()
            return i[1]
    fil.close()
    return -1
 
def write_to_file(navn,konsert,antall,filnavn):
    pris = payment(int(get_price(konsert)),antall)
    fil = open(filnavn,'a')
    fil.write(konsert+';'+str(antall)+';'+str(pris)+';'+navn+'\n')
    fil.close()
 
def ticket(navn,konsert,antall):
    return([navn,konsert,antall,payment(int(get_price(konsert)),antall)])
print(ticket("jo","The Rectorats",8))
 
 
write_to_file("jo","The Rectorats",8,'billetter.txt')

#listeduplicates

def removeDup(liste):
    nyliste = []
    for i in liste:
        if i not in nyliste:
            nyliste.append(i)
    return nyliste

#multi
def multi(n):
    table = []
    for i in range(1,1+n):
        table.append([])
        for j in range(1,1+n):
            table[i-1].append(j*i)
    return table
 
for i in multi(5):
    print(i)


#isPrime?
from math import sqrt
 
def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    i = 3
    while i<= sqrt(n):
        if n%i==0:
            return False
        i+=1
    return True
 
print(isPrime(101))


#Setduplicate remover

def removeDup(liste):
    return list(set(liste))

#Skøyter
def mshd2s(minutter, sekunder, hundredeler):
    return (minutter*60+sekunder+0.01*hundredeler)
 
def rundeTid(startTid,sluttTid):
    startSek = mshd2s(startTid[0],startTid[1],startTid[2])
    sluttSek = mshd2s(sluttTid[0],sluttTid[1],sluttTid[2])
    return sluttSek-startSek
 
def alleRundeTider(passeringsTider):
    rundetider = []
    for i in range(len(passeringsTider)-1):
        rundetider.append(rundeTid(passeringsTider[i],passeringsTider[i+1]))
    return rundetider
 
print(alleRundeTider([[0,20,0],[0,50,10],[1,21,21],[1,53,33]]))

#Telefonkatalog

def leggTilNummer(navn,nummer,katalog):
    if navn in katalog:
        katalog[navn].append(nummer)
    else:
        katalog[navn] = [nummer]
    return katalog
 
 
def finnNumre(navn,katalog):
    if navn in katalog:
        return katalog[navn]
    return -1

#Terning

from random import randint
 
 
def snittKast(n):
    total = 0
    i = 0
    while i < n:
        total += randint(1, 6)
        i += 1
    return float(total)/n
 
 
print(snittKast(20))

    

