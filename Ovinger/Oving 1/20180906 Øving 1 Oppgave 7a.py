#Oppgave 7a Øving 1
from turtle import *
import time

# Lar bruker velge farge 
print("Choose colour. Important that you only use english")
print("""Exampel colours "blue" and "cyan".""")
print("You can find all colours on: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm") 

x = input("Input background colour ")
y = input("colour ")

# setter opp tegnevinduet
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)
 
# velger farger
bgcolor(x)
color(y)
 
#tegner den indre firkanten
begin_fill()
right(10) # tilter den 10 grader nedover
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()
  
time.sleep(10)      # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder
