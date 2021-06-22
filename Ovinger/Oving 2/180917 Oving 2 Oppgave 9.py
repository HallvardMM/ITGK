
import time
from turtle import *

# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
penn=str(input("Velg pennefarge, NTNU-rosa (R) eller NTNU-turkis (T): "))
fyll=str(input("Fyllfarge, NTNU-gul (G), -oransj (O), -lilla (L): "))
opp=str(input("Ønsker du spissen på trekanten opp eller ned (O / N)? "))
if penn=="R":
    penn="#ad208e"
else:
    penn="#5cbec9"

if fyll=="G":
    fyll="#d5d10e"
elif fyll=="O":
    fyll="#f58025"
else:
    fyll="#552988"

if opp=="O":
    pensize(7)          # sett pennen 7 piksler tykk
    pencolor(penn)    # sett pennefargen til rosa
    bgcolor("#00509e")     # sett bakgrunnsfargen grå
    fillcolor(fyll) # sett fyllfargen lilla
# Tegner en fylt trekant
    begin_fill()
    forward(200)        # gå 100 piksler framover
    left(120)           # drei 120 grader venstre
    forward(200)  
    left(120) 
    forward(200)
    end_fill()

else:
    pensize(7)          # sett pennen 7 piksler tykk
    pencolor(penn)    # sett pennefargen til rosa
    bgcolor("#00509e")     # sett bakgrunnsfargen grå
    fillcolor(fyll) # sett fyllfargen lilla
# Tegner en fylt trekant
    begin_fill()
    forward(200)        # gå 100 piksler framover
    right(120)           # drei 120 grader venstre
    forward(200)  
    right(120) 
    forward(200)
    end_fill()
# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(5)
