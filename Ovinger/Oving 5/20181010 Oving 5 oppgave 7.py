#Øving 5 oppgave 7a)

def divisiable(a,b):
    if a%b==0:
        c=True
    else:
        c=False
    return c

#print(divisiable(10,3))
#print(divisiable(10,5))

#Oppgave 7b) #kan ikke sjekke om 2 er primtall

def isPrime(a):
    for b in range(2,a):
        if divisiable(a,b)==True:
            c=False
            break
        else:
            c=True
    return c

#print(isPrime(15))
#print(isPrime(11))

#Oppgave 7c)

def isPrime2(a): #kan ikke kjøre tall mindre enn 9
    for b in range(3,round(a**(0.5)+0.5),2):
        if divisiable(a,b)==True:
            c=False
            break
        else:
            if divisiable(a,2):
                c=False
            else:
                c=True
    return c

print(isPrime2(9))
print(isPrime2(15))
