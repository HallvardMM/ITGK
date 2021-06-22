#Øving 2 oppgave 1e)
alder = int(input("Din alder: "))
if alder < 3:
    print("Gratis")
elif alder < 12:
    print("Billettpris: 30")
elif alder < 26:
    print("Billettpris: 50kr")
elif alder < 67:
    print("Billettpris: 80kr")
else:
    print("Billettpris: 40kr") 
