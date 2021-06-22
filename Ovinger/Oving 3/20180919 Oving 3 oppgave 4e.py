#Øving  3 Oppgave 4e)
#*
#**
#***
#****
#*****
i = 5
for x in range(i): #0,1,2,3,4
    for y in range(x+1):#1,2,3,4,5
        print("*", end="")#printer ut like mange stjerner som y er. "End" gjør slik at stjernene er på form ** ikke under hverandre
    print()#skaper linjeskift for hver nye stjernerekke
