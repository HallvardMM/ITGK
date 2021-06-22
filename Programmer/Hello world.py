print('Hello world')#Hello world
print(4)#4
print(2>3)#False
print(2<3)#True
#Fuck this code
print("I'am a yellow frog")#For å skrive med apostrof
print("""I'am a green "frog" """)#For å både ha ' og " i teksten

print("""Han sa: "Her blir det mye 'fnutter'!" """)#Oppgave

#Variabler er et navn som representerer en verdi lagret i datamaskinens minne.

alder = 23 #setter variablen alder lik 23
print(alder) #Printer vaiablen. Python er casesensetiv pass på stor og liten bokstav.
alder = 24 #setter variablen på nytt
print(alder)#printer 24

#Ikke bruk tall, mellomrom eller nøkkelord(print, if etc.) som variabler. Første tegn må være en bokstav eller "_".

#RAM Random Acsess Memory 8 Bits i en byte

elever = 250
Ansatte_Gløs = 13

print("skolen har", elever, "elever")

#Pseodokode epler og bananer
Epler = 23
Bananer = 12
print("antall epler", Epler)
print("antall bananer", Bananer)
Epler = 43
Bananer = 17
print("antall epler", Epler)
print("antall bananer", Bananer)

# Datatyper
# heltall(int)
# Desimaltall(float) Bruker punktum, ikke komma.
# Tekststreng(str) Navn = 'Petter'
# Sannhetsverdi(bool) True eller False

print(type(Epler))#printer hva "typen" til variablen alder er.

#Du kan skrive 5.9e9 som betyr 5.9*10**9

Navn = input('Hva er navnet ditt? ')#Spør om hva navnet til personen er slik at de kan skrive det inn.
print('Hei!',Navn)

heltall = int(input("Gi meg et heltall!"))

desimaltall = float(input("Gi meg et desimaltall"))

print(heltall+desimaltall)

Streng_verdi = input('Hvor mange kuer har du?')
kuer = int(Streng_verdi)

#Oppgave

Navn = input("Hva er navnet ditt? ")

Gammel = int(input("Hvor gammel er du, "+Navn+"? "))

print("Hei,", Navn+".", "Du blir", Gammel+10, "om 10 år!")

#Matte operasjoner: + pluss - minus * gange / dele // % rest ** opphøyd

#Gjennomssnitsberegning

X = int(input("Første måling "))
Y = int(input("Andre måling "))
Z = int(input("Tredje måling "))
print("gjennomssnittet er")
print((X+Y+Z)/3)            


