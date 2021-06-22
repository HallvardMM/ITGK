#kont 2016
# 1b,2c,3c,4c,5d,6b,7a,8a,9c,10a,11c,12a,13d,14d,15d,16d,17b,18a,19c,20b
# alt riktig

#2a
def load_bin(filename):
    binstring=""
    try:
        with open(filename,'r') as f:
            for line in f:
                binstring+=line.strip()             
    except:
        print("Error: Could not open file ",filename)
    return binstring

#2b
def bin_to_dec(binary):
    lengde=len(binary)
    summen=0
    binnummer=1
    for i in range(lengden-1,-1,-1):
        if binary[i]=="1":
            decimal+=binnumber
        binnumber+=binnumber
    return summen

#2c
def dec_to_char(dec):
    liste=[' ',',','.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',',R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']
    if dec<len(liste) and dec>0:
        return liste[dec-1]
    else:
        return ""

#2d
def bin_to_txt(binstring):
    txt=""
    for i in range(0,len(binstring),5):
        desi=bin_to_dec(binstring[i:i+5])
        txt += dec_to_car(desi)
    return txt
#2e
def main():
    print("Binary-to-text converter")
    b_file=input("Name of binary file to load from: ")
    b_string=load_bin(b_file)
    txt=bin_to_txt(b_string)
    t_file=input(str("Name of text file to save to: "))
    try:
        with open(t_file,'w') as f:
            f.write(txt)
            print(b_file,"has been converted and saved to",t_file)
    except:
        print('Error: Could not write to file', t_file)
    
#3a
def sek_paa_benken(ant_paa_laget,ant_paa_banen,kamptid):
    sek=kamptid*60
    reserver=ant_paa_laget-ant_paa_banen
    benk=(sek/ ant_paa_laget)*reserver
    return round(benk)

#3b
def minutt_sekund(sekunder):
    sek=sekunder%60
    minutt=sekunder//60
    if sek>9:
        print(str(minutt)+":"+str(sek))
    else:
        print(str(minutt)+":0"+str(sek))
#3c
def les_inn_forfall():
    liste=[]
    spiller=" "
    print("Skriv navn, eller kun ENTER (tom tekst) for å avslutte.")
    while len(spiller)>0:
        spiller=input("Spiller som har meldt forfall: ")
        liste.append(spiller)
    return liste

#3d
def finn_tilgjengelige(alle,forfall):
    tilgjengelige=[]
    for barn in alle:
        if barn not in forfall:
            tilgjengelige.append(barn)
    return tilgjengelige

#3e
def laginndeling(spillere, sp_per_lag):
    import random
    kopi=[]+spillere
    ant_lag=len(spillere)//sp_per_lag
    lagoppsett = [ [] for i in range(ant_lag)]
    lag=0
    while kopi !=[]:
        navn = random.choice(kopi)
        kopi.remove(navn)
        lagoppsett[lag].append(navn)
        lag = (lag +1) % ant_lag
    return lagoppsett

#3f
def main():
    forfall=les_in_forfall()
    strlag=int(input("Spillere per lag: "))
    kamptid=int(input("Kamptid (minutter): "))
    tilgjengelige=finn_tilgjengelige(BARN,forfall)
    lag=laginndeling(tilgjengelige, strlag)
    for i in range(len(lag)):
        print("Lag",i+1,"\n",lag[i],"\ntid på benken per spiller:",minutt_sekund(sek_paa_benken(len(lag[i]),strlag,kamptid)),"\n")

#3g
def ny_fil(navn,lesfil,skrivfil):
    tekst=""
    f=open(lesfil,"r") 
    for line in f:
        if navn in line:
            test+=line
    f.close()
    g=open(skrivfil,"w"):
        g.write(tekst)
    g.close()
    return utfil

#4a
# printer gangetabellen i 5x5 format.
# funksjonen gjør det opp til den verdien man gir inn

#4b
# output [[3,2,1],[5,4,3]]
# lager en ny matrise med to interne lister og endrer tallene es polassering.

#4c
#returnerer 120
#regner ut input! (i dette tilfelle 5!)
# den returnerer "nynorsk"
# tar bokstaver fra ordet først [0],[1],[3],[6],[10],[15],[21]


        
            
        

