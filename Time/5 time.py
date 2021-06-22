"""Forelesing uke 40
Bibliotek math, turtle, random
import math - import random as r - math.sin r.random
from math import sqrt, sin - sqrt(x) eller sin(x)
from random import random - random()
ikke anbefalt - from math import * - kan være problematisk ved skrivefeil

modulen random er egentlig pseudo random
Random er bra for spill, statiske analyser, autogenerert kunst og musikk
random.seed(),random.random(),random.uniform(fra,til (flyttall))
,random.randint(fra,til),

Void- og reutverdi-funksjoner
void - returnerer ikke en verdi - print(),turtle.circle(r),random.seed()
returenerer verdi - input(),abs(-5), len("hei"), random.random(1,6),math.sqrt(9)

Skrive egne funksjoner med returverdi
def funksjonsnavn (para1, para2, para3):
    mer kode skal inn her...
    return uttrykk """

# C:\Users\hallv\OneDrive\Dokumenter\Hallvard\Skole\1. semester\ITGK\Python\Programmer

#cmath bruker "j" ikke "i" for sqrt(-1)

"""Uttrykk bak return
- hva som helst som gir en verdi - kan returnere int, float, bool, str, list osv.
- returnere flere verdier? - return uttrykk1, uttrykk2"""

def get_name():
    first_name=input("fornavn")
    last_name=input("etternavn")
    return first_name, last_name

#variabels skop er den delen av programmet hvor variablen kan brukes
#Parameter står i funksjonsdefinisjonen, argumentet i kallet

def overlap(a,b,c,d):
    if c >= b or a >= d:
        svar = False
    else:
        svar = True
    return svar

def overlap_v2(a,b,c,d, incl_ends):
    return 
    

# eller def overlap(a,b,c,d):
#    return a < d and c < b
