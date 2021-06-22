def sjekk_svar(spm):
    var = input(spm)
    if var == "hade":
        skriv_statistikk(F, M, fag, ITGK, timer, antall)
        kjør = False
    else:
        return var

def sjekk_alder(spm):
    while True:
        var = sjekk_svar(spm)
        alder = int(input("Hvor gammel er du? "))
        if alder < 16 or alder > 25:
            print("Du kan dessverre ikke ta denne undersøkelsen")
            print()
            print("Velkommen til spørreundersøkelsen!")
            print()
            continue
        else:
            return var, alder

def les_streng(spm):
    while True:
        var, alder = sjekk_alder(spm)
        if var == "f":
            return M, F + 1, alder
        elif var == "m":
            return M + 1, F, alder

def les_ja_nei(spm):
    M, F, alder = les_streng("Hvilket kjønn er du? [f/m]: ")
    while True:
        var = sjekk_svar(spm)
        if var == "ja":
            while True:
                if int(alder) > 21:
                    spm = "Tar du virkelig ITGK?: "
                else:
                    spm = "Tar du ITGK? [ja/nei]: "
                var = sjekk_svar(spm)
                if var == "ja":
                    return M, F, alder, ITGK + 1, fag + 1
                elif var == "nei":
                    return M, F, alder, ITGK, fag + 1
        elif var == "nei":
            return M, F, alder, ITGK, fag


def les_tall(spm):
    var = int(sjekk_svar(spm))
    return timer + var, antall + 1

def skriv_statistikk(F, M, fag, ITGK, timer, antall):
    print("Resultat av undersøkelse!")
    print("  Antall kvinner: " + str(F))
    print("  Antall menn: " + str(M))
    print("  Antall personer som tar fag: " + str(fag))
    print("  Antall personer som tar ITGK: " + str(ITGK))
    print("  Antall timer i snitt brukt på lekser: " + str(float(timer/antall)))


M = 0
F = 0
alder = 0
ITGK = 0
fag = 0
timer = 0
antall = 0
kjør = True

while kjør==True:
    print()
    print("Velkommen til spørreundersøkelsen!")
    print()
    fag_gammel = fag
    M, F, alder, ITGK, fag = les_ja_nei("Tar du et eller flere fag? [ja/nei]: ")
    if fag > fag_gammel:
        timer, antall = les_tall("Hvor mange timer bruker du daglig (i snitt) på lekser?: ")
                         
    
    
            
        
