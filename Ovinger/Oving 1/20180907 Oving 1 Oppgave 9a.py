#Øving 1 oppgave "Vitenskapelig notasjon"
stoff=str(input("Si et stoff du er i besittelse av: "))
mol_gram=float(input("Hva er molvekt i gram for "+stoff+"? "))
gram=float(input("Hvor mange gram vann har du? "))
molekyler=format((gram/mol_gram)*(6.022e23),'.1e')
print("Du har "+str(molekyler)+" molekyler "+str(stoff))
