#øving 6 oppgave 2


while True:
    Oppgave = str(input("Hvilken oppgave ønsker du? (a/b/c/end) "))

    if Oppgave == "end":
        break

    elif Oppgave == "a":
        def is_six_at_edge(x):
            is_six_at_edge=x
            return is_six_at_edge[0]==6 or is_six_at_edge[-1]==6:
        
        print(is_six_at_edge([1,2,3,4,5,6,7]))

    elif Oppgave == "b":
        def average(x):
            average_liste=x
            c=sum(average_liste)/len(average_liste)
            return c

        print(average([1,3,5,7,9,11]))

    elif Oppgave == "c":
        def median(x):
            median_liste=x
            median_liste.sort()
            d=len(median_liste)
            c=median_liste[int(d/2)]
            return c

        print(median([1,2,4,5,7,9,10]))
        print(median([1,4,2,5,3]))
        
