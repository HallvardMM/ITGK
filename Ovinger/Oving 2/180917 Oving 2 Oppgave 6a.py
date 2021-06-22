# Øving 2 Oppgave 6a
pos = input("sett inn en posisjon fra et sjakkbrett ")# byttes ut med en input()-setning
 
bokstav = pos[0]           #gir variabelen bokstav verdi 'a'
 
tall = int(pos[1])              #gir variabelen tall verdi 5

if (bokstav == "a" or bokstav == "c" or bokstav == "e" or bokstav == "g") and (tall == 1 or tall == 3 or tall == 5 or tall == 7):
        print("Svart")
if ((bokstav == "b" or bokstav ==  "d" or bokstav ==  "f" or bokstav ==  "h") and (tall == 2 or tall == 4 or tall == 6 or tall == 8)):
        print("Svart")
if ((bokstav == "a" or bokstav ==  "c" or bokstav ==  "e" or bokstav ==  "g") and (tall == 2 or tall == 4 or tall == 6 or tall == 8)):
        print("Hvit")
if ((bokstav == "b" or bokstav ==  "d" or bokstav ==  "f" or bokstav ==  "h") and (tall == 1 or tall == 3 or tall == 5 or tall == 7)):
        print("Hvit")
else:
        print("error")

