#The doorman
navn=(input("Hva heter du? "))
alder=int(input("Hvor gammel er du? "))
full=str(input("Er du full? "))
if alder>=18:
    print("Du er gammel nok")
else:
    print("Du er for ung "+str(navn))
if alder>=18 and (full=="Ja" or full=="JA" or full=="ja"):
    print("Du slipper ikke inn fordi du er for full")
if alder>=18 and (full=="Nei" or full=="NEI" or full=="nei"):
    print("Velkommen inn "+str(navn))
if (full=="nEi" or full==
    "NeI"):
    print('Du er full som skriver "nei" på en slik måte')

