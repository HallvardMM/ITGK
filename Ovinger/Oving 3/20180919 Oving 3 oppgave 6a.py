#Øving 3 oppgave 6a)
from turtle import *
import time
from random import random,  randint

while True:
    oppgave=str(input("Hvilken oppgave ønsker du (a/b/c/d/e/f/g/h): "))

    if oppgave=="a":
        wn=Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        for i in range(4):
            forward(100)
            left(90)
        time.sleep(2)

    elif oppgave=="b":
        wn=Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        for i in [16,13,10,7,4,1]:
            pensize(i)
            forward(20)
        time.sleep(2)

    elif oppgave=="c":
        wn=Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        for i in range(250,0,-7):
            forward(i)
            left(90)
        time.sleep(2)

    elif oppgave=="d":
        wn=Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        print("Jeg kan tegne et regulært polygon.")
        kanter=int(input("Velg antall kanter: "))
        omkrets=int(input("Velg omkrets på polyginet: "))
        for i in range(kanter):
            forward(omkrets)
            left(360/kanter)
        time.sleep(2)

    elif oppgave=="e":
        wn=Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        print("Jeg kan tegne et regulært polygon.")
        kanter=int(input("Velg antall kanter: "))
        omkrets=int(input("Velg omkrets på polyginet: "))
        antall=int(input("Velg antall "+str(kanter)+"-kanter i blomsten: "))
        for i in range(antall):
            for i in range(kanter):
                forward(omkrets/kanter)
                left(360/kanter)
            left(360/antall)
        time.sleep(2)

    elif oppgave=="f":
        wn=Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        pensize(5)
        R,G,B = random(), random(), random()
        tilt = random() + 0.5
        sides = randint(5,9)
        for i in range(300):
            x = (300-i)/300
            color(R, G, B)
            forward(i)
            left(360/sides + tilt)
            R,G,B = 1-R, 1-G, 1-B
            tilt*=0.2
            if i>=100:
                tilt+=2
        time.sleep(2)

       
        
