# Øving 5 oppgave 2
while True:
    Oppgave=str(input("Hvilken oppgave ønsker du? (a/b/c/d/end) "))
    if Oppgave=="end":
        break

    elif Oppgave=="a":
        # Skriv funksjonen din her
        def absol(x):
            if x>=0:
                x=x
            else:
                x=-x
            return x
  
        # skript for å teste funksjonen:
        print("Absoluttverdien til 5 er", absol(5))
        print("Absoluttverdien til -3 er", absol(-3))
        print("Absoluttverdien til 0 er", absol(0))

    elif Oppgave=="b":
        # skriv funksjonen din her
        def knop2km_t(knop):
            knop=knop*0.514444444
            knop=knop*3.6
            return knop
  
        # skript
        knop = float(input("Oppgi fart i knop: "))
        km_t = knop2km_t(knop)
        print("Det blir", round(km_t, 2), "km/t")

    elif Oppgave=="c": #Får to desimaler skjønner ikke hvorfor eksempel ikke får det. Kan bruke round()?
        # skriv funksjonen din her
        def imp2cm(fot, tommer):
            tommer=12*fot+tommer
            cm=tommer*2.54
            return cm

        # skript
        fot = int(input("Oppgi antall fot: "))
        tommer = int(input("Oppgi antall tommer: "))
        cm = imp2cm(fot, tommer)
        print("Det blir", cm, "cm")

    elif Oppgave=="d":
        # skriv funksjonen cmyk2rgb() her øverst
        def cmyk2rgb(C,M,Y,K):
            R = 255 * (1-C) * (1-K)
            G = 255 * (1-M) * (1-K)
            B = 255 * (1-Y) * (1-K)
            return R, G, B
  
        print("Oppgi farge i CMYK og få det konvertert til RGB.")
        C = float(input("C: "))
        M = float(input("M: "))
        Y = float(input("Y: "))
        K = float(input("K: "))
        R, G, B = cmyk2rgb(C, M, Y, K)
        print("Som RGB:", round(R), round(G), round(B)) #round() for å pass eksempel
          
        # viser fargen på skjermen:
        from turtle import colormode, bgcolor
        colormode(255)
        bgcolor(int(R), int(G), int(B))
