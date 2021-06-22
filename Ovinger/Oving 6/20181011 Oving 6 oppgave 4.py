#øving 6 oppgave 4
import turtle, time
turtle.speed(100)

oddetall=[]
for i in range(1,20,2):
    oddetall.append(i)

print(oddetall)

my_string = str(input("Give me ten colours! (remember (, ) behind every colour) "))
my_list = my_string.split(', ')
print(my_list)



for i in range(len(oddetall)): # Skjønner ikke helt hva de mener med: "Deretter skal du gå gjennom alle tallene i listen med oddetall fra 0 til 20. For alle tallene skal du hente ut en farge fra listen med farger,"
    farge=my_list[i]
    turtle.setposition(0,0)
    turtle.color(farge)    
    for w in range(0,41):
        turtle.forward(len(oddetall)*oddetall[i])
        turtle.left(123) 

time.sleep(10)
