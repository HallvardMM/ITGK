# Øving 7 oppgave 4

while True:

    oppgave=str(input("hvilken oppgave a/b/c/d/end "))
    oppgave=oppgave.lower()

    if oppgave=="end":
        break

    #Oppgave a
    elif oppgave=="a":
        def uppernowhite(streng):
            streng=streng.upper().rstrip().lstrip()
            return streng

        streng = " \n  The Sky's Awake So I'm Awake  \t  "
        print(uppernowhite(streng))
        print()

    #Oppgave b
    elif oppgave=="b":
        def splitonch(streng,ch):
            streng1 = streng.split(ch)
            return streng1

        streng = "Hakuna Matata"
        karakter = 'a'

        print(splitonch(streng,karakter))
        print()


    #Oppgave c
    elif oppgave=="c": #sjekker om "eat" er i s2 med små bokstaver. Siden den er det endres s og den nye s printes ut.
        s1 = "eat"
        s2 = "I want to be like a caterpillar. Eat a lot. Sleep for a while. Wake up beautiful."
        def func(s1, s2):
            s = "My bed is a magical place where I suddenly remember everything I forgot to do."
            if s1 in s2.lower():
                s = "The more you weigh, the harder you are to kidnap. Stay safe. Eat cake."
            print(s)
  
        func(s1,s2)

    #Oppgave d
    elif oppgave=="d":
        for i in range(1,8):
            print('Z'*i)
        for y in range(8,0,-1):
            print('Z'*y)
        
