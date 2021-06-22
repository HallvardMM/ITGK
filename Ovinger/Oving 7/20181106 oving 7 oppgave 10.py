#Øving 7 oppgave 10
#a
def p_ig(t, v, n, rgas=8.31452):
    return(t*n*rgas)/v


print(p_ig(373.15,2.4,100))     #Legg merke til at man IKKE trenger å sende inn en konstant for rgas (men man kan om man ønsker), siden denne blir satt til 8.31452 om det ikke blir gitt et argument
print(p_ig(293,24*10**(-3),1))

#b

def p_ig_pptable(v,t, n):
    tab = []
    for i in range(len(v)):
        vol = v[i]
        tab.append([vol])
        for j in range(len(t)):
            temp = t[j]
            p = p_ig(temp, vol, n)
            tab[i].append(p)
    return tab


#Kjøring av koden:
nv = 10     # number of volumes (rows)
nt = 3      # number of temperatures (columns)
 
n = 10      # [mol]
t = [100 + float(j)*200 for j in range(nt)]     # [K]
v = [10**(-float(i)/nv) for i in range(1, nv+1)]
 
table = p_ig_pptable(v,t,n)
 
print(table)

#c

#Oppgave c
nv = 10     # number of volumes (rows) [-]
nt = 3      # number of temperatures (columns) [-]
 
n = 10      # [mol]
t = [100 + float(j)*200 for j in range(nt)]     # [K]
v = [10**(-float(i)/nv) for i in range(1, nv+1)]
 
table = p_ig_pptable(v,t,n)
 
print("| Volum (m^3)".ljust(21),"|",("Temp. = "+str(t[0])+"K").ljust(19),"|",("Temp. = "+str(t[1])+"K").ljust(19),"|",("Temp. = "+str(t[2])+"K").ljust(19),"|")
print("-"*89)
 
#SKRIV DIN KODE HER
for lst in table:
    print('|',end=' ')
    for el in lst:
        print(str(el).ljust(19),"|",end =' ')
    print("\n")

