#Øving 6 oppgave 7a

fasit=['A','C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'C', 'D']

#Oppgave 7b


def sjekk_svar(x):
    poeng=0
    for i in range(len(fasit)):
        if fasit[i]==x[i]:
            poeng=poeng+1
        else:
            poeng=poeng
    return (poeng/20)*100

print(sjekk_svar(['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'A', 'C']))
print(sjekk_svar(fasit))
print(sjekk_svar(['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])) 

    
