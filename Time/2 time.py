alder=int(input("Hvor gammel er du? "))
b=int(18)
print(alder,b,sep='\n\t')
#\n \t \' \'' \\
print(format(1/3,'.2f'))
print(format(1/3,'10.1f'))
print(format(1/3, 'e'))
print(format(1/3,'.0%'))
print(format(500,'10d'))
#mindre eller lik <=
# er lik ==
# er ulik !=
# a=5 tilordner variablen a verdi 5, a==5 sjekker om a er 5
if alder>=18 and alder<=64:
    print("Du skal ha voksenbillet!")
elif alder>64:
    print("Du skal ha honnørbillet!")
else:
    print("Du skal ha barnebillet!")

passord =input("Skriv inn ditt passord: ")
if passord == "nuff":
    print("Riktig")

else:
    print("galt")

if "A"<"B":
    print("Bokstaven A er mindre enn bokstaven B")
ord_1=str(input("Skriv et ord "))
ord_2=str(input("Skriv et nytt ord "))
if ord_1==ord_2:
    print("Du har jo valgt samme ord...")
elif ord_1<ord_2:
    print("Første ord kommer først i alfabetet")
elif ord_1>ord_2:
    print("Andre ord kommer først i alfabetet")
else:
    print("Error") #Unødvendig i denne koden, men kanskje brukbart ved andre eksempler
#Logiske operatorer "and", "or", "not"






