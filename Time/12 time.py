#Siste time før eksamen! ! ! !

#filbehandling(tekstfiler og binærfiler), unntak/exceptions, to-dimensjonale lister, dictionaries, strengbehnadling

# Filbehandling
# f=open(filenavn,"r") 
# for line in f:
# f.close()

#mye snacks på powerpointen

#Exceptions

# myue snacks på powerpoint

def les_fil(filnavn):
    try:
        f=open(filnavn,"r")
        liste=f.read()
        f.close()
        return liste
        

    except FileNotFoundError: #kunne også brukt IOError
        return None


print(les_fil('hovedsteder.txt').split(','))



tekst_som_str=str(les_fil('hovedsteder.txt'))

def streng_til_fil(streng):
    liste=streng.split(',')
    sluttliste=[]
    for element in liste:
        liste2=element.split()
        sluttliste.append([liste2[0]," ".join(liste2[1:])])
    return sluttliste

print(streng_til_fil(tekst_som_str))


def skriv_ut_liste(liste):
    for element in liste:
            print("Hovedstaden i",element[0],"er",element[1])

skriv_ut_liste(streng_til_fil(tekst_som_str))

def spm(liste):
    from random import randint
    liste=liste
    while len(liste)>0:
        riktig=False
        while riktig==False:
                element=liste[randint(0,len(liste)-1)]
                svar=input("Hva er hovedstaden i "+str(element[0])+": ")
                if svar.lower()==element[1].lower():
                    print("Det er korrekt!")
                    riktig=True
                    liste.remove(element)
                else:
                    print("Det er feil!")

#spm(streng_til_fil(tekst_som_str))

            
def liste_til_dict(liste):
    ordbok={}
    for element in liste:
        ordbok[element[0]]=element[1]
    return ordbok

print(liste_til_dict(streng_til_fil(tekst_som_str)))

#Røverspråk


def rover(tekst):
    nyteskt=''
    tekst=tekst.split()
    for bokstav in tekst:
        if 
    



