# Øving 7 oppgave 2

while True:

    oppgave=str(input("hvilken oppgave a/b/c/d/end "))
    oppgave=oppgave.lower()

    if oppgave=="end":
        break

    
    #Oppgave a
    elif oppgave=="a":
        def combinestr(s1,s2):
            s3=s1+" "+s2
            return s3

        s1 = "James"
        s2 = "Bond"

        print(combinestr(s1,s2))
        print()

    #Oppgave b
    elif oppgave=="b":
        def nospace(liste):
            bokstav = ""
            for streng in liste:
                bokstav +=streng
            return bokstav

        liste = ["abc","defg","hijklm","nop"]
        print(nospace(liste))
        print()

    #Oppgave c
    elif oppgave=="c":
        def firstletter(liste):
            for i in range(0,len(liste)):
                print(liste[i][0])
                
        liste = ["UKA","lever","videre"]
        firstletter(liste)
        print()
        
    #Oppgave d
    elif oppgave=="d":

        def func1(liste): #Denne tar 3. bokstaven fra ordet hvis det er lengre
            streng = "" #enn 3
            for s in liste:
                if len(s)>3:
                    streng += s[3]
            return streng #returnerer bob
  
        def func2(streng): #Denne funksjonen legger strengen med seg selv to ganger
            streng += streng
            return streng #returnerer bobob
          
        print(func2(func1(["Klabert","Oslo","Tur","stubbe"]))) #blir bobbob
        
