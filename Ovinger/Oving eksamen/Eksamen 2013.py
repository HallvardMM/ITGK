#Eksamen 2013
#2a
def chess_match():
    total_score1=0
    total_score2=0
    num_games=int(input("Hvor mange partier skal det spilles? "))
    if num_games<1:
        print("Så kjedelig, da blir det ingen kamp")
    else:
        for i in range(1,num_games+1):
            print("Parti",i)
            score1=float(input("Hvor mange poeng til spiller 1? "))
            score2=float(input("Hvor mange poeng til spiller 2? "))
            total_score1+=score1
            total_score2+=score2
    print("Kampen er slutt!\nSpiller 1 fikk",total_score1,"poeng\nSpiller 2 fikk",total_score2,"poeng")

#2b
def end_of_match(num_games, game, total_score1, total_score2):
    if total_score1>num_games/2:
        return 1
    elif total_score1>num_games/2:
        return 2
    elif game==num_games:
        return 3
    else:
        return 0
#2c
def chess_scorer():
    score1=float(input("Resultatet til spiller 1: "))
    while score1 not in (0,0.5,1):
        print("umulig resultat!")
        score1=float(input("Resultatet til spiller 1: "))
    return score1,1-score1

#2d
def player_score(results):
    score=0
    for element in results:
        if element !=None:
            score+=element
    return score

# 3a
# returnerer a er 3 og b er 2. Den ser hvor mange ganger man kan trekke b fra a.
# og returnerer det svaret samt antall ganger trukket fra.
# også kjent som heltallsdivisjon og rest...

# 3b
# returnerer listen som [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
# hvis listens elementer er like lang som listen sorterer radverdi til kolonneverdi og motsatt hvis ikke -1

# 3c
# returnerer 000101001000 gjør om hex til bi

#4a
def payment(pris,antall):
    if antall>3:
        return round(pris*antall*0.9,2)
    else:
        return round(pris*antall,2) #rounder for å få gjort det om til kr og øre
#4b
def get_price(konsert):
        liste=[]
        f=open('prices.txt','r') #bruker ikke try/except fordi vi har file
        for line in f:
            k1=line.split(';') #k1 er hver enkel konsert
            liste+=k1
        f.close()
        for i in range(0,len(liste),2):
            if konsert == liste[i]:
                return liste[i+1]
            else:
                return -1
#4c
def ticket(navn,konsert,billetter):
    print("*"*41+"\nUka 2015"+"*"*41)
    pris=payment(get_price(konsert),biletter)
    vs=['Navn:',navn,'Konsert:',konsert,'Antall billetter:',biletter,'Totalpris:',pris]
    for i in range(0,len(vs),2):
        print(i.rjust(16)+str(i+1).rjust(25))

#4d
def write_to_file(navn,konsertnavn,antall,filnavn):
    pris=payment(getprice(konsertnavn),antall)
    f=open(filnavn,'a')
    f.write(str(konsertnavn)+";"+str(antall)+";"+str(pris)+";"+str(navn)+"\n")
    f.close()


    
            
    
    
