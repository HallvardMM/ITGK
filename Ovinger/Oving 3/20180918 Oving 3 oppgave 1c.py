#Øving 3 oppgave 1c
print("Du har 42 bokstaver til disposisjon.")
tall=42
while tall > 0:
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
    if  tall>0:
        tall=int(tall-len(adj))
        print("Du har",tall, "bokstaver til disposisjon.")  
print("Takk for nå!")
    
