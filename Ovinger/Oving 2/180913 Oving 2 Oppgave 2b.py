#Øving 2 oppgave 2b)
navn1 = str(input("Første navn: "))
navn2 = str(input("Andre navn: "))
print("Under følger navnene i alfabetisk rekkefølge:")
if navn1 <= navn2:
    print(str(navn1)+"\n"+str(navn2))
else:
    print(str(navn2)+"\n"+str(navn1))
#Gidder ikke ta hensyn til æøå
