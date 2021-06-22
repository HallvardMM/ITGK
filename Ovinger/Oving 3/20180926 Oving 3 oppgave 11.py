# Øving 3 siste oppgave

import random

while True:
    oppgave = str(input("Hvilken oppgave a/b/c/d/e "))

    if oppgave == "a":
        for i in range(1, 6):
            for x in range(1, i+1):
                print(x, end=" ")
            print()

    elif oppgave == "b":
        for i in range(1,6):
            for x in range(1, 2):
                print('#' + str((" ")*i) + '#')

    elif oppgave == "c":
        tall=int(input("Skriv inn et positivt heltall: "))
        gammel_tall=tall
        listen=[]
        y=2
        for i in range(1,tall+1):
            for x in range(y,i+1):
                if tall%x==0:
                    tall=tall//x
                    listen.append(str(x))
                    break
                y=x#For å ikke måtte sjekke tall før siste x funnet.
        if len(listen) == 1:
            print(gammel_tall, "er et primtall.")
        else:
            str1 = '*'.join(listen)
            print(gammel_tall, "=", str1)

        # Kunne også gjort det sånn https://stackoverflow.com/questions/16996217/prime-factorization-list

    elif oppgave == "d":
        forsøk=3
        x=0
        Y=0
        while forsøk>0:
            x=random.randint(0,9)
            y=random.randint(0,9)
            z=x*y
            svar=int(input("Hva blir,"+str(x)+"*"+str(y)+"?"))
            if svar==z:
                print("Gratulerer, det er helt riktig!")
                mer=int(input("Er det ønskelig med flere oppgaver? 0 for ja 1 for nei: "))
                if mer==1:
                    break
            else:
                forsøk-=1
                print("Dessverre ikke riktig. Du har "+str(forsøk)+" forsøk igjen.")
        print("Dessverre klarte du ikke regne det stykke, men vent så får du et nytt et :)")
