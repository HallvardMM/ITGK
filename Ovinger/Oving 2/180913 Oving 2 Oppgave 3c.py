#Øving 2 oppgave 3c)
print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))
  
if p>10 or p<0:
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10-p
    print("Da blir det",p,"på deg og",r,"på meg :D")
