#Øving 6 oppgave 1

while True:
    Oppgave = str(input("Hvilken oppgave ønsker du? (a/b/c/d/e/end) "))

    if Oppgave == "end":
        break

    elif Oppgave == "a":
        my_first_list=[1, 2, 3, 4, 5, 6]
        print(my_first_list)

    elif Oppgave == "b":
        my_first_list=[1, 2, 3, 4, 5, 6]
        print(my_first_list[5])
        print(my_first_list[-1]) #Dette er den andre måten

    elif Oppgave == "c":
        my_first_list=[1, 2, 3, 4, 5, 6]
        my_first_list[4]='pluss'
        print(my_first_list)

    elif Oppgave == "d":
        my_first_list=[1, 2, 3, 4, 5, 6]
        my_first_list[4]='pluss'
        my_second_list=my_first_list[3:]
        print(my_second_list)

    elif Oppgave == "e":
        my_first_list=[1, 2, 3, 4, 5, 6]
        my_first_list[4]='pluss'
        my_second_list=my_first_list[3:]
        print(my_second_list, "er lik 10")
