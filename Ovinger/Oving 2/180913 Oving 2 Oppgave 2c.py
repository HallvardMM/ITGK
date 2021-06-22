#Øving 2 oppgave 2c)
#Kodesnutt 1: k er større en b fordi det er senere i alfabetet
if 'k' < 'b':
    print('k er mindre enn b')
else:
    print('k er større enn b')
  
  
#Kodesnutt 2: l er før n i alfabetet så "Los Angeles" så "New York"
ny = "New York"
la = "Los Angeles"
  
if ny < la:
    print(ny)
    print(la)
else:
    print(la)
    print(ny)
  
  
#Kodesnutt 3: printer bare "druer" fordi de er like
d1 = "DRuEr"
d2 = "drUer"
if d1.lower() < d2.lower():
    print(d1)
    print(d2)
else:
    print(d2.lower())
