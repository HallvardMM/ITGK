#Øving 3 oppgave 5a)
import random
nedre=int(input("Gi en nedre grense for det tilfeldige tallet: "))
øvre=int(input("Gi en øvre grense for det tilfeldige tallet: "))
tilfeldigtall = random.randint(nedre,øvre)
gjett=tilfeldigtall+1
forsøk=0

while gjett!=tilfeldigtall:
    gjett=int(input("Make a guess: "))
    if gjett>tilfeldigtall:
        print("The correct number is lower")
    elif gjett<tilfeldigtall:
        print("The correct number is higher")
    forsøk+=1
print("You guessed correct! You used", forsøk,"tries!")
