#Oppgave 7b øving 1
from turtle import *
import time

# Lar bruker velge farge 
print("Choose colour. Important that you only use integers from 0 to 16777215")
print("""Exampel colours "123423" and "45678".""")
print("You can find all colours on: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm") 

x = int(input("Input background colour "))
y = int(input("colour "))

Rb=int((x//256)//256)
Gb=int((x//256)%256)
Bb=int((x%256)//256)

Rf=int((y//256)//256)
Gf=int((y//256)%256)
Bf=int((y%256)//256)

# setter opp tegnevinduet
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)
 
# velger farger
colormode(255)
bgcolor(Rb,Gb,Bb)
color(Rf,Gf,Bf)
 
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
  
time.sleep(8)      # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder

