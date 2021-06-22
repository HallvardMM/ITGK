#Time uke 42
#liste1.append([14,15]) legger til [14,15] på slutten av listen.
#liste1.extend([14,15]) legger til 14, 15 på slutten av listen.

#Sette to lister lik hverandre
liste1=[1,2,3,4]
liste2=[]
for item in liste1:
    liste2.append(item)

listu1=[1,2,3,4]
listu2=[]+listu1

print(liste2,"\n",listu2)

students=[['joe','kim'],['sam','sue'],['kelly','chris']] #ligner en matrise
print(students)
print("",['joe','kim'],"\n",['sam','sue'],"\n",['kelly','chris'])

#lag en 2-demsjonal 10x10 matrise med 0er

tabell_10x10 = [[0 for col in range(10)] for row in range(10)]
print(tabell_10x10)

tabell_3d = [[[1 for x in range(3)] for y in range(3)] for z in range(3)]
print(tabell_3d)

print()

# Oppgave

tabell=[[0 for col in range(3)] for row in range(3)]
#evnt: tabell = [[0,0,0],[0,0,0],[0,0,0]]

tall=2
for row in range(3):
    for col in range(3):
        tabell[row][col]=tall
        #print(tabell) #bare for å sjekke tabellen
        #vent=input() #venter til jeg trykker enter
        tall+=2

for row in tabell:
    print(row)

print()

#Kap. 7.9 Tupler

#Tupler som lister bare at de ikke kan tukles med. De er ikke-mutarebare

liste_1000=[i+1 for i in range(1000)]

liste_3gangen_1000=[i+3 for i in range(0,1000,3)]

#Kapittel 8 Strenger

streng="jeg er kul"
print(streng[4]) #printer e fordi mellomrom tas med

print()

#oppgave strenger


def skriv_tegn_indeks(tekst,tegn):
    for x in range(len(tekst)):
        if tekst[x]==tegn:
            print(x)


skriv_tegn_indeks("apekatt","a")

#Strenger er ikke-muterbare! De lager heller en ny streng.

tekst="Die eaz nfu test"
print(tekst[::2]) #printer annenhvert tegn

s="ITGK"
print(s.endswitch('GK'))
print(s.find('TG'))
print(s.replace('GK', '-grunnkurs'))
print(s.startswitch('IT'))






