# Øving 7 oppgave 1

while True:

    oppgave=str(input("hvilken oppgave a/b/c/end "))

    if oppgave=="end":
        break

    
    #Oppgave a
    elif oppgave=="a":
        word='Discoworld'
        for ch in word:
            print(ch)
        print()

    #Oppgave b
    elif oppgave=="b":
        def thirdletter(word):
            if len(word)<=2:
                print('q')

            else:
                print(word[2])

        thirdletter("mistborn")
        thirdletter("IT")

    #Oppgave c
    elif oppgave=="c":
        def largestindex(word):
            a=len(word)-1
            return a

        print(largestindex("The Way of Kings"))
        print(largestindex("Elantris"))
        
