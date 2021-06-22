# Oppgave 10 øving 3
hemmelig_ord = str(input("Hemmelig ord er? "))
hemmelig_ord = hemmelig_ord.lower()
antall_liv = int(input("Hvor mange liv? "))
listen = list(hemmelig_ord)
listto = list(len(hemmelig_ord)*"_")

print("\n"*50+"Hangman: "+"_ "*len(hemmelig_ord))
print("Du har antall liv", antall_liv)
while antall_liv>0:
    bokstav = str(input("Gjett på én bokstav i ordet: "))
    bokstav = bokstav.lower()
    if bokstav in listen:
        print("Stemmer, bokstaven er i ordet")
        for n in range(0, len(hemmelig_ord)):
            if listen[n] == bokstav:
                listto[n] = bokstav
        str1 = ' '.join(listto)
        print(str1)
    else:
        print("Bokstaven", bokstav,"er ikke i ordet.")
        antall_liv += -1
        if antall_liv <= 0:
            print("Mannen falt og ble hengt! ╭( ✖_✖ )╮")
        print("Du har antall liv", antall_liv)
    if listto == listen:
        print("Gratulerer, du klarte ordet! Det var " + str(hemmelig_ord) + ". Mannen ble ikke hengt")
        print("(╯°□°）╯︵ ┻━┻")
        break
    
