import copy

def return_brikke(brett, i):
    if brett[i] == 0:
        return "⬜"
    elif brett[i] == 1:
        return "♟"
    elif brett[i] == 2:
        return "♝"
    elif brett[i] == 3:
        return "♞"
    elif brett[i] == 4:
        return "♜"
    elif brett[i] == 5:
        return "♛"
    elif brett[i] == 6:
        return "♚"
    elif brett[i] == -1:
        return "♙"
    elif brett[i] == -2:
        return "♗"
    elif brett[i] == -3:
        return "♘"
    elif brett[i] == -4:
        return "♖"
    elif brett[i] == -5:
        return "♕"
    elif brett[i] == -6:
        return "♔"

def print_sjakkbrett(brett):
    print("# | | A| B|C| D| E|F| G| H| \n _|_|__|__|_|__|__|_|__|__|", end=" ")
    for j in range(8):
        print("\n" + str(j+1) + " | ", end="|")
        for i in range(j*8, (j+1)*8):
            print(return_brikke(brett, i), end="|")
    print()

def returner_posisjon_som_tall(posisjon):
    while True:
        posisjon = posisjon.split()
        if posisjon[0].lower() == "a":
            tall = (int(posisjon[1])-1) * 8
            return tall
        elif posisjon[0].lower() == "b":
            tall = 1 + (int(posisjon[1])-1) * 8
            return tall
        elif posisjon[0].lower() == "c":
            tall = 2 + (int(posisjon[1])-1) * 8
            return tall
        elif posisjon[0].lower() == "d":
            tall = 3 + (int(posisjon[1])-1) * 8
            return tall
        elif posisjon[0].lower() == "e":
            tall = 4 + (int(posisjon[1])-1) * 8
            return tall
        elif posisjon[0].lower() == "f":
            tall = 5 + (int(posisjon[1])-1) * 8
            return tall
        elif posisjon[0].lower() == "g":
            tall = 6 + (int(posisjon[1])-1) * 8
            return tall
        elif posisjon[0].lower() == "h":
            tall = 7 + (int(posisjon[1])-1) * 8
            return tall

def finn_kolonne(posisjon, i):
    if (8 + posisjon + i) % 8 == 0:
        bok = "a"
    elif (8 + posisjon + i) % 8 == 1:
        bok = "b"
    elif (8 + posisjon + i) % 8 == 2:
        bok = "c"
    elif (8 + posisjon + i) % 8 == 3:
        bok = "d"
    elif (8 + posisjon + i) % 8 == 4:
        bok = "e"
    elif (8 + posisjon + i) % 8 == 5:
        bok = "f"
    elif (8 + posisjon + i) % 8 == 6:
        bok = "g"
    elif (8 + posisjon + i) % 8 == 7:
        bok = "h"
    return bok

def finn_rad(posisjon, i):
    rad = str(((posisjon + i) // 8) + 1)
    return rad

def returner_tall_som_posisjon(posisjon, konstant, i, key):
    stige = ((24 + konstant) % 8)
    bok = finn_kolonne(posisjon, konstant * i)
    if stige > 4 and ord(bok) > ord(key[0]):
        return "ugyldig"
    elif stige < 4 and ord(bok) < ord(key[0]):
        return "ugyldig"
    rad = finn_rad(posisjon, konstant * i)
    if int(rad) <= 0:
        return "ugyldig"
    elif int(rad) > 8:
        return "ugyldig"
    pos = str(str(bok) + " " + str(rad))
    return pos

def alle_konstanter(tur, brett):
    if tur % 2 == 1:
        venn = [1, 2, 3, 4, 5, 6]
        fiende = [-1, -2, -3, -4, -5, -6]
    else:
        fiende = [1, 2, 3, 4, 5, 6]
        venn = [-1, -2, -3, -4, -5, -6]        
    for i in range(64):
        if brett[i] in venn:
            bok = finn_kolonne(i, 0)
            rad = finn_rad(i, 0)
            key = str(bok) + " " + str(rad)
            if brett[i] == 1:
                tall = i
                if tall in range(8, 16):
                    v = 3
                else:
                    v = 2
                k = [8]
                konstanter[key] = k
                variabler[key] = v
            if brett[i] == -1:
                tall = i
                if tall in range(48, 56):
                    v = 3
                else:
                    v = 2
                k = [-8]
                konstanter[key] = k
                variabler[key] = v
            if brett[i] in [2, -2]:
                k = [-9, -7, 7, 9]
                konstanter[key] = k
                v = 8
                variabler[key] = v
            if brett[i] in [3, -3]:
                k = [-17, -15, -10, -6, 6, 10, 15, 17]
                konstanter[key] = k
                v = 2
                variabler[key] = v
            if brett[i] in [4, -4]:
                k = [-8, -1, 1, 8]
                konstanter[key] = k
                v = 8
                variabler[key] = v
            if brett[i] in [5, -5]:
                k = [9, 8, 7, 1, -1, -7, -8, -9]
                konstanter[key] = k
                v = 8
                variabler[key] = v
            if brett[i] in [6, -6]:
                k = [9, 8, 7, 1, -1, -7, -8, -9]
                konstanter[key] = k
                v = 2
                variabler[key] = v
    return venn, fiende
                        
def alle_trekkene(brett, venn, fiende):
    for key in konstanter:
        start = returner_posisjon_som_tall(key)
        konstantliste = konstanter[key] 
        for j in range(len(konstanter[key])):
            konstant = konstantliste[j]
            if brett[start] == 1:
                if start + 7 <=63 and (start + 7) % 8 != 7 and brett[start + 7] in fiende:
                    if key not in alle_trekk:                      
                        alle_trekk[key] = [returner_tall_som_posisjon(start, 7, 1, key)]
                    elif key in alle_trekk:                       
                        alle_trekk[key].append(returner_tall_som_posisjon(start, 7, 1, key))
                if start + 9 <=63 and (start + 9) % 8 != 0 and brett[start + 9] in fiende:
                    if key not in alle_trekk:                      
                        alle_trekk[key] = [returner_tall_som_posisjon(start, 9, 1, key)]
                    elif key in alle_trekk:                       
                        alle_trekk[key].append(returner_tall_som_posisjon(start, 9, 1, key))
            elif brett[start] == -1:
                if start - 7 >=0 and (start - 7) % 8 != 0 and brett[start - 7] in fiende:
                    if key not in alle_trekk:                      
                        alle_trekk[key] = [returner_tall_som_posisjon(start, -7, 1, key)]
                    elif key in alle_trekk:                       
                        alle_trekk[key].append(returner_tall_som_posisjon(start, -7, 1, key))
                if start - 9 >=0 and (start - 9) % 8 != 7 and brett[start - 9] in fiende:
                    if key not in alle_trekk:                      
                        alle_trekk[key] = [returner_tall_som_posisjon(start, -9, 1, key)]
                    elif key in alle_trekk:                       
                        alle_trekk[key].append(returner_tall_som_posisjon(start, -9, 1, key))
            for i in range(1, variabler[key]):
                pos = returner_tall_som_posisjon(start, konstant, i, key)
                if pos == "ugyldig":
                    break
                if start + konstant * i >= 64 or start + konstant * i < 0:
                    break
                if key not in alle_trekk and brett[start + konstant * i] not in venn:                      
                    alle_trekk[key] = [pos]
                elif key in alle_trekk and brett[start + konstant * i] not in venn:                       
                    alle_trekk[key].append(pos)
                elif brett[start + konstant * i] != 0:
                    break
                if brett[start + konstant * i] in fiende:
                    break
        
def velgbrikke(brett):
    while True:
        key = str(input("Skriv inn ønsket brikke [mellomrom mellom kolonne og rad]: "))
        if key in egne_trekk:
            posisjon = returner_posisjon_som_tall(key)
            return egne_trekk[key], posisjon
        else:
            print("Du har ikke valgt en gyldig brikke")
            continue

def gjør_trekk(brett):
    while True:
        print_sjakkbrett(brett)
        trekk, gammel_posisjon = velgbrikke(brett)
        brikke = return_brikke(brett, gammel_posisjon)
        svar = str(input("Du har valgt en " + str(brikke) + "\nMulige trekk er " + str(trekk) + "\nVennligst velg et trekk: "))
        if svar.lower() in trekk:
            posisjon = returner_posisjon_som_tall(svar)
        else:
            continue
        return posisjon, gammel_posisjon    

def kongepos(brett, tur):
    if tur % 2 == 1:
        venn = [1, 2, 3, 4, 5]
        konge = 6
        fiende = [-1, -2, -3, -4, -5, -6]
    else:
        fiende = [1, 2, 3, 4, 5, 6]
        venn = [-1, -2, -3, -4, -5]
        konge = -6
    for j in range(64):
        if brett[j] == konge:
            return konge, venn, fiende, j

def kongesjakk(konge, venn, fiende, posisjon):
    sjakk = ""
    for key in alle_trekk:
        trekk = alle_trekk[key]
        for i in range(len(trekk)):
            konge_posisjon = returner_posisjon_som_tall(trekk[i])
            if konge_posisjon == posisjon:
                sjakktrekk = []
                angreps_posisjon = returner_posisjon_som_tall(key)
                pos = trekk[i]
                kongekomp = pos.split(" ")
                angkomp = key.split(" ")
                sjakk = "sjakk"
                raddiff = int(angkomp[1]) - int(kongekomp[1])
                kolonnediff = ord(angkomp[0]) - ord(kongekomp[0])
                mulige_konstanter = list(konstanter[key])
                for j in range(1, 8):
                    variabel = None
                    for k in mulige_konstanter:
                        konstant = k
                        if (int(konge_posisjon) - int(angreps_posisjon)) / (konstant * int(j)) == 1:
                            variabel = int(j)
                            break
                    if variabel != None:
                        break
                print("Rad:", raddiff, "\nKolonne:", kolonnediff, "\nKonstant og variabel: ", konstant, variabel)
                for y in range(variabel):
                    trekket = returner_tall_som_posisjon(angreps_posisjon, konstant, y, key)
                    sjakktrekk.append(trekket)
                return pos, sjakk, key, sjakktrekk
            else:
                pos = trekk[i]
    return pos, sjakk, key, []

def sjakkmatt(brett, kongeposisjon, angriper, sjakktrekk, konge, venn, fiende, posisjonstall):
    del egne_trekk[kongeposisjon]
    mulige_trekk = sjakktrekk
    for konstant in [-9, -8, -7, -1, 1, 7, 8, 9]:
        posisjonen = returner_tall_som_posisjon(posisjonstall, konstant, 1, kongeposisjon)
        if posisjonen != "ugyldig":
            kongpos = returner_posisjon_som_tall(posisjonen)
            pos, sjakk, key, trekk = kongesjakk(konge, venn, fiende, kongpos)
            if sjakk != "sjakk":
                mulige_trekk.append(posisjonen)
        egne_trekk[kongeposisjon] = mulige_trekk
    return mulige_trekk

brett = [4, 3, 2, 6, 5, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -4, -3, -2, -6, -5
         , -2, -3, -4]

tur = 0
while True:
    tur += 1
    nytt_brett = []
    egne_trekk = {}
    konstanter = {}
    variabler = {}
    alle_trekk = {}
    venn, fiende = alle_konstanter(tur, brett)
    alle_trekkene(brett, venn, fiende)
    egne_trekk = copy.deepcopy(alle_trekk)
    konstanter = {}
    variabler = {}
    alle_trekk = {}
    venn, fiende = alle_konstanter(tur + 1, brett)
    alle_trekkene(brett, venn, fiende)
    konge, venn, fiende, tall = kongepos(brett, tur)
    kongeposisjon, sjakk, angriper, trekk = kongesjakk(konge, venn, fiende, tall)
    if sjakk == "sjakk":
        print()
        print("Sjakk")
        print()
        sjakktrekk = sjakkmatt(brett, kongeposisjon, angriper, trekk, konge, venn, fiende, tall)
        nye_trekk = copy.deepcopy(egne_trekk)
        for key in egne_trekk:
            mulige_trekk = []
            dine_trekk = egne_trekk[key]
            for i in range(len(dine_trekk)):
                if dine_trekk[i] in sjakktrekk:
                    mulige_trekk.append(dine_trekk[i])
            if mulige_trekk != [] and key != kongeposisjon:
                nye_trekk[key] = mulige_trekk
            else:
                del(nye_trekk[key])
        if nye_trekk == {}:
            print("Sjakkmatt")
            break
        else:
            egne_trekk = {}
            egne_trekk = copy.deepcopy(nye_trekk)
            for key in egne_trekk:
                print(key, end=": ")
                for q in range(len(egne_trekk[key])):
                    print(egne_trekk[key][q], end=" | ")
                print()
    posisjon, gammel_posisjon = gjør_trekk(brett)
    nytt_brett = copy.deepcopy(brett)
    nytt_brett[posisjon], nytt_brett[gammel_posisjon] = nytt_brett[gammel_posisjon], 0
    alle_trekk = {}
    venn, fiende = alle_konstanter(tur + 1, nytt_brett)
    alle_trekkene(nytt_brett, venn, fiende)
    konge, venn, fiende, tall = kongepos(nytt_brett, tur)
    kongeposisjon, sjakk, angriper, trekk = kongesjakk(konge, venn, fiende, tall)
    if sjakk == "sjakk":
        print("Du satte deg selv i sjakk")
        continue
    brett = copy.deepcopy(nytt_brett)
