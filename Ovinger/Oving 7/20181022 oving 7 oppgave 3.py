# Øving 7 oppgave 3

while True:

    oppgave=str(input("hvilken oppgave a/b/c/d/end "))
    oppgave=oppgave.lower()

    if oppgave=="end":
        break

    
    #Oppgave a
    elif oppgave=="a":
        def fourthletter(liste):
            y=liste[::4]
            return y

        streng="I Was Told There’d Be Cake"
        print(fourthletter(streng))
        print()

    #Oppgave b
    elif oppgave=="b":
        def twolastletters(liste):
            y=''
            for i in range(0,len(liste)):
                y=y+liste[i][-2:]
            return y

        liste = ["sabel","kan","mestr","kuleis"]
        print(twolastletters(liste))
        print()
        
    #Oppgave c

    #Kodesnutt 1
    streng = "I Want Cake"
    streng[7:] = "Cupcake" # feil
    print(streng)
     
    #Kodesnutt 2
    streng = "I Want Cake"
    streng = streng[-4:100:] #kjører selvom det er en merkelig føring
    print(streng)
    
    #Kodesnutt 3
    streng = "I Want Cake"
    streng = streng[:] #manglet noe i []
    print(streng)
