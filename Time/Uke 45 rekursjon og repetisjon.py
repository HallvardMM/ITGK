# ITGK rekursjon og repetisjon
# Repetisjon øving 9
# Feilhåndtering, (vanlige feil IndexError, KeyError, FileNotFoundError, AttributeError)
def get_index_value_from_list(liste,i):
    try:
        return liste[i]
    except IndexError:
        return -1

# Kan bruke "finally" tilslutt (vet ikke hvordan den virker) tror virker som else.

#Gjør bursdagsdatabasen oppgaven

birthdays = {
"22 nov": ["Bob Bernt", "Mathias"],
"10 des": "Elle",
"31 okt": ["Aragusta", "Carina"],
"12 jan": "Silje",
"23 okt": "Willy",
"5 jul": ["Martin", "Øystein"],
"11 mar": "Miriam"
}

def add_birthday_to_date(date, name):
    try:
        birthdays[date].append(name)
    except AttributeError:
        birthdays[date] = [birthdays[date],name]
    except KeyError:
        birthdays[date] = name

add_birthday_to_date("12 jan", "Sindre")
add_birthday_to_date("9 feb", "Lillian")
print(birthdays)

#Filhåndering
#Filen må alltid lukkes! Kan bruke with så slipper du å skrive f.close()
#filoperasjoner, "r","w","a"
# linjer=[]
# Åpner filen med variablen file
# with open("file.txt","r") as file:

#Oppgave om dictionaries og filter
#Et firma har lagret infor om sine ansatte i en tekstfil. Filen består av et ukjent antall linjer på formen:
#"<ansatt_id>;<fornavn> <etternavn>;<alder>;<e-post>,<lønn>" Lønn med desimaltall og punktum

# mitt forsøk
def les_fra_fil(fil):
    dic={}
    with open(fil,"r") as file:
        for r in readlines.fil():
            y=r.split(";")
            dic[y[0]]=y-y[0]
    return dic

# hans forsøk
def read_employee_file(filename):
    employees={}
    try:
        with open(filename) as file:
            for line in file.readlines():
                line=line.strip()
                line=line.split(";")
                IDen = int(line[0])
                rest_info=line[1:]
                employees[IDen] = rest_info
                
    except FileNotFoundError:
        print("fil ikke funnet")
    return employees

print(read_employee_file("ansatte.txt"))

def send_christmas_mail(employees):
    mails = []
    for key, value in employees.items():
        name = value[0]
        mail = value[3]
        salary = float(value[4])
        text = "Hei! " + name + "\nGod Jul!: Gratulerer med nye kr " + str(salary//10) + "i julebonus"
        mail = [text,mail]
        mails.append(mail)

    return mails

#Rekursjon
# En funksjon kaller seg selv med andre argumenter enn det ble klat med selv
# Viktig at man har en case der funksjonen vil returnere uten å kalle seg selv, ellers vil vi fortsette i evig tid (eller til man stopper prosessen)

#def recursive(var):
#    if conditon for termination:
#        return var #Can return
#        #Here, you can do something with var
#    return var * recursive(var-1)

def recursive(n):
    if n == 0:
        return 1
    return n*recursive(n - 1)

def iterative(n):
    prod = 1
    for i in range(2,n+1):
        prod *= i
    return prod

def fibbonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonacci(n-1)+fibbonacci(n-2)

print(fibbonacci(20))

#Oppgave 1
def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*fac(n-1)
print(fac(6))

def binominal(n,k):
    return fac(n)/(fac(k)*fac(n-k))

print(binominal(4,2))


#Oppgave 2
#mitt forsøk
def sum_list(liste):
    sum=0
    if isinstance(liste, list):
        for i in liste:
            if isinstance(i,list):
                sum_list(i)
            else:
                y=y+sum(i)
    return y

#hans forsøk
def sum_chaos(liste):
    summen=0
    for element in liste:
        if isinstance(element,list): #Sjekker om element er en list
            summen += sum_chaos(element)
        else:
            summen += element
    return summen

print(sum_chaos([2,3,[4,7,[2,[3]]]]))


def reversed_list(liste):
    if len(liste) == 1:
        return liste
    return [liste[-1]]+reversed_list(liste[0:-1])

print(reversed_list([5,6,2,1]))
