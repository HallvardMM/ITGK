#Øving 3 oppgave 1g
from turtle import *
var=int(input("Hvilken vinkel ønsker du? "))
vinkel = var
x=2
while not x<=0.1: #Bruker 0.1 ikke 1 fordi da minskes sannsynligheten for at den stopper utenfor  nullpunkt. Eks 179 grader
    forward(5000/vinkel) #la til en null for mer visuell tilfredstillelse
    left(vinkel)
    x=abs(xcor())+abs(ycor()) #abs av hver verdi kontra for begge samlet for å minske sannsynligheten for at den stopper lengre unna nullpunkt
    
#Hvordan kan vi være sikker på at den ikke stopper når pilen er veldig nærme (0.0,0.0)?
