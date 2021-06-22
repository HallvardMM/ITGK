#Time uke 39
#Pensum simple functions
from math import pi
#def funksjonsnavn_navn():
#    kode
#    kode
#    etc.

def melding(): #Definerer en funksjon
    print("Her er en funksjon")
    print("Som skriver til konsollet")
melding()# kan kalle på funksjonen senere i programmet

def kvadrat():
    tall=int(input("Trenger et heltall: "))
    print(tall**2)

kvadrat()


def main(): #Lager en hovedfunksjon som kaller på de andre funksjonene
    melding()
    kvadrat()

def divi_to():
    tall=float(input("Skriv inn et tall "))
    print(tall/2)

def multi_to():
    tall=float(input("Skriv inn et tall "))
    print(tall*2)

def main_2():
    multi_to()
    divi_to()

main_2()


def main_3():
    r=eval(input("Hva er radius? "))
    areal_sirkel(r,pi)

def areal_sirkel(r,pi):
    A=pi*(r**2)
    print("En sirkel med radius", r,"har areal", format(A,".2f"))


main_3()


