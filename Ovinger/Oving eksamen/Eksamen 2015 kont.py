#Kont 2015 Eksamen
#1d,2d,3a,4c,5b(feil),6d,7c,8c,9a,10a,11a,12a,13b,14a,15c,16b,17b,18d,19b,20b
#5c mottager kan oppdage, men ikke korrigere, endringer av tallene under overføring

# 2a
#[25.0, 20.0, 20.0, 13.33, 15.0]
#Funksjonen tricky_a finner snittet av tre og tre nærliggende verdier, samt på endene snittet av
#to nærliggende verdier i ei liste

# 2b Returner False
# Sjekker om en verdi i listen er =(verdien før+1)

# 2c sjekker om x er i funksjonen og returnerer rad*kolne for denne posisjonen
# 2

# 3a
from random import randint
def throw(n):
    liste=[]
    for i in range(n):
        liste.append(randint(1,6))
    return liste
#3b
def chance(dice):
    summen=0
    for element in dice:
        summen+=element
    return summen

#3c
def house(dice):
    dice.sort()
    if (dice[0]!=dice[-1]) and (dice[0]==dice[1] and dice[2]==dice[3]==dice[4]) or (dice[0]==dice[1]==dice[2] and dice[3]==dice[4]):
        return chance(dice)
    else:
        return 0

#3d
def straight(dice):
    correct=[1,2,3,4,5,6]
    dice.sort()
    if dice==correct[:5]:
        return 15
    elif dice==correct[1:6]:
        return 20
    else:
        return 0
        

#4a
def lesinbilinfo():
    merke=input("Hvilket bilmerke var det? ")
    modell=input("Hvilken modell? ")
    farge=input("Hvilken farge? ")
    return [merke,modell,farge]
    
#4b
def sjekk_bil(vitne,faktisk):
    sant=True
    for i in range(len(vitne)):
        if not (vitne[i]==faktisk[i] or vitne[i]=='?'):
            sant=False
    return sant

#4c
SKILTBOKSTAV = ('A','B','C','D','E','F','G','H','J','K','L','N','P','R','S','T','U','V','X','Y','Z','?')
def les_gyldig_skilt():
    gyldig=False
    while not gyldig:
        streng=input('Skriv inn skilt, 2 bokst + 5 tall (?=usikker) ')
    if len(streng)!=7:
        print('Skiltnummer må være 7 tegn langt')
    elif (streng[0] not in SKILTBOKSTAV or streng[1] not in SKILTBOKSTAV):
        print('To første tegn må være skiltbokstav eller ?')
    elif (streng[2:7] != '?????' and not streng[2:7].replace('?','').isdigit()):
        print('Fem siste tegn må være tall eller ?')
    else:
        gyldig=True
    return streng

#4d
def match(vitne,faktisk):
    sant=True
    for i in range(vitne):
        if vitne[i]!=faktisk[i] or vitne[i]!='?':
        sant=False
    return sant

#4e
def match_liste(vitne,liste):
    match=[]
    for element in liste:
        if match(vitne,element):
            match.append(element)
    return match

#4f
def les_biler_fra_fil(filnavn):
    fil=open(filnavn,'r')
    dic={}
    for linje in fil:
        linje=linje.strip('\n')
        liste=linje.split()
        dic[liste[0]] = liste[1:]
        fil.close()
    return dic

def match_bildata(vitneskilt,bilinfo,bil_db):
    kandidater=[]
    mulige_skilt = match_liste(vitneskilt,bil_db.keys())
    for skilt in mulige_skilt:
    if sjekk_bil(bilinfo,bil_db[skilt]):
        kandidater.append(skilt)
    return kandidater

def vis_resultat(skiltliste):
    if skiltliste == []:
        print('Ingen match')
    else:
        print('Mulige kjøretøyer er:')
    for element in skiltliste:
        print(element, 'Eier:', bil_db[element][3])


def main():
    try:
        bil_db = les_biler_fra_fil('biler.txt')
        print('Fil lest')
    except Exception as feil:
        print('Problemer med lesing av fil, feilmelding:')
        print(feil)
    else:
        fortsett=True
        while fortsett:
            bilinfo = les_inn_bilinfo()
            regnr = les_gyldig_vitneskilt()
            skiltliste = match_bildata(regnr,bilinfo,bil_db)
            vis_resultat(skiltliste)
            svar = input('Vil du sjekke flere kjøretøyer? (J/N) ')
            if svar.upper() == 'N':
                fortsett = False
main()
