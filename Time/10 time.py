#Time 10 Algoritmer i praksis
#pensum "starting out with Python" kap.12 "theory book IT Grunnkrus" kap.5


#Algoritme-effektivitet
#store o, store omega, stor theta

#Sekvensielt søk
#søke gjennom en liste etter en verdi. "Brute-force"
#Fordelen er at det fungerer på en usortert liste

#oppgave

def seq_serch(liste,n):
    y=False
    for x in liste:
        if (x==n):
            y=True
            break
    return y
        
print(seq_serch([1,2,3,4,5],5))
print(seq_serch([1,2,3,4,5],6))   

#Brute -force fungerer raskest når første element er det vi leter etter

# Innstikkssortering
# Enkel sorteringsalgoritme som sorterer en liste element for element
# Ganske enkel å programmere

#oppgave

def insertion_sort(liste):
    for i in range(1,len(liste)):
        element = liste[i]
        hull=i
        while(hull>0 and liste[hull-1]>element):
            liste[hull]=liste[hull-1]
            hull=hull-1
            liste[hull] = element
    return liste

print(insertion_sort(['Petter','Alex','Diana','Bodil','Anne']))

#Best-case nesten sortert liste der bare en må byttes om. (Big thetha 1)
#Worst-case alle må bytte (big theta n**2)


# Kap.12 (starting out with Python) rekursjon
# En rekursiv funksjon er en funksjon som kaller seg selv.
# Rekursive funksjoner brukes ofte i algoritmer for å lage elegante løsninger på problemet
# Viktig å ha en Stoppverdi!!!

def countdown_for(antall):
    for i in range((antall),-1,-1):
        print("teller ned:", i)

def countdown_while(antall):
    i = antall
    while i >=0:
        print("teller ned:", i)
        i=i-1

def countdown_recursive(antall):
    if (antall>-1): #Skall bare kjøre når antall > -1
        print("teller ned:", antall)
        countdown_recursive(antall-1)#kaller seg selv med ny verdi

print("\nfor-loop:")
countdown_for(5)
print("\nwhile-loop:")
countdown_while(5)
print("\nrekursiv funksjon:")
countdown_recursive(5)
    
#Rekrusiv for kalkulering av fakultet n!
print()

#fakultet
def fac(n):
    if(n==0):
        return 1
    else:
        return n * fac(n-1)
print(fac(4))
# print(fac(992)) #max-verdi før error!

# Binærsøk
def bin_search(liste,n,mini,maxi):
    if maxi < mini:
        return False
    else:
        midtpunkt = (maxi-mini//2)
        if (n < liste[midtpunkt]):
            return bin_search(liste,verdi,mini,midtpunkt-1)
        elif (n > liste[midtpunkt]):
            return bin_search(liste,verdi,midtpunkt+1,maxi)
        else:
            return midtpunkt


print(bin_search([1,2,3,9,11,13,17,25,57,90],57,0,10-1))

#Tidsbruk Bestcase første valg (theta 1) worst-case siste valg(theta log(n))


        





















