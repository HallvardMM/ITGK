# Øving 5 oppgave 4
while True:
    Oppgave=str(input("Hvilken oppgave ønsker du? (Del A/ Del B/ Del C /end) "))
    if Oppgave=="end":
        break

    elif Oppgave=="Del A":
        GRAVITY=9.81
        def get_fall_time(d):
            t=(2*d/GRAVITY)**0.5
            return t

        d=float(input("Antallet meter objektet skal ramle: " ))
        get_fall_time(d)
        print("Det tar", get_fall_time(d),"sekunder å ramle", d,"meter")

    elif Oppgave=="Del B":
        GRAVITY=9.81

        def set_gravity(gravity):
            global GRAVITY
            GRAVITY = gravity

        def get_fall_time(d,gravity):
            t=(2*d/GRAVITY)**0.5
            return t
        
        set_gravity(9.67)

        print(get_fall_time(20)) # Skjønner ikke hvorfor eks gir 1,438...


#"""Svar B. Nei blir rotete at globale variabler skal endres hele tiden.
# bedre om globale variabler kun er konstanter"""

    elif Oppgave=="Del C":
        GRAVITY=9.81

        def get_fall_time(d,y=GRAVITY): #Kunne også gjort det med y=9.81 for å slippe global variabel
            t=(2*d/y)**0.5
            return t
        
        print(get_fall_time(20)) 
        print(get_fall_time(20, 1.62))
