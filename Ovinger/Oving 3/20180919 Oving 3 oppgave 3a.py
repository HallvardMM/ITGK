# Øving 3 Oppgave 3a)
stud = int(input("Hvor mange studenter? "))
emne = int(input("Hvor mange emner? "))
x=0
y=0
for x in range(stud):
    for y in range(emne):
        print("Stud",x+1,"elsker Emne", y+1,";", end=" ")    
    print()
