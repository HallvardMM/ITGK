# Eksamen 2016
# Flervalg:
# 1c, 2c, 3d, 4c, 5c, 6a, 7a, 8d, 9a, 10b, 11c, 12c, 13c, 14a (feil), 15a, 16a, 17c, 18b, 19d, 20c, 21d, 22b, 23b, 24d, 25a
# 14b riktig . "Den digitale dividende": betegnelsen på ledige (ikke-tildelte) frekvensressurser i det elektromagnetiskespektrum

# 2a flopp returnerer verdiene endret fra 0 til 1 og fra 1 til 0 i matrisen.
# skriver ut [[1,0,1],[0,1,0],[1,0,1]]

# 2b tar inn et årstall på formen (d,m,y) og returnerer det på formen 30th Nov 133, hvor dagen vil få riktig ending st hvis f.eks 21st og 22nd 23rd 24th og høyere.
# 30th Nov 1337

# 2c Den returnerer antall bokstaver av den med mest og hva bokstaven er på formen ('antall','bokstaven')
# output 3 b

# 2d printer 6
# tar summen av siffrene til summen av siffrene til input

#3a
DISTRICTS = 92
parties = ['Tea Party', 'Coffee Party', 'Milk Party',
 'House Party', 'Beach Party']
def initElection():
    tabell=[[0]*len(parties)]*DISTRICTS
    return tabell

print(initElection())

#3b
def updateElection(tabell,nrdistrikt,liste):
    for i in range(len(liste)):
        tabell[nrdistrikt][i]+=liste[i]
    return tabell

#3c
def printLeadP(election):
    leder=[0]*len(election[0])
    for i in range(len(election)):
        for y in range(len(leder)):
            leder[y]+=election[i][y]
    print (parties[leder.index(max(leder))],"is leading the election with "+str(max(leder)),"votes.")
#Antar her at det skal vises hvor mange stemmer partiet har ikke hvor mange stemmer de leder over neste parti.


printLeadP([[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]])

#3d
def leadIndex(votes):
    lead = 0
    for i in range(1, len(votes)):
        if votes[i] > votes[lead]:
            lead = i
    return lead

def sumDelegates(election):
    d = [0] * (len(election[0]) + 2)
    for row in election:
        if sum(row) == 0: # no votes yet
            d[-1] += 1 # count in last element
        else:
            i = leadIndex(row) # from 3c
            if row[i] in row[i+1:]: # max also further right
                d[-2] += 1 # count as tie
            else: # only one winner
                d[i] += 1 # count for party i
    return d

def printResults(election):
    nd = sumDelegates(election)
    t = parties + ['Undecided (tied)'] + ['Undecided (no votes)']
    for i in range(len(t)):
        print((t[i]+':').ljust(30), format(nd[i], '3d'), end=' ')
    if nd[i] == 1:
        print('delegate')
    else:
        print('delegates')

#4a
D = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
L = [ 1000000, ' million', 1000, ' thousand', 1, '']

def i2_txt(inter):
    if inter%10 == 0:
        return D[inter]
    else:
        return D[inter-inter%10]+"-"+D[inter%10]

#4b
def i3_txt(inter):
    if len(str(inter))<3:
        return i2_txt(inter)
    else:
        bak=inter%100
        først=inter-inter%100
        hundre=først/100
        return D[hundre]+" hundred "+i2_txt(bak)

#4c
def i9_txt(inter):
    for i in range(0, len(L), 2):
        if inter >= L[i]:
            text += ' ' + i3_txt(inter//L[i]) + L[i+1]
            inter = inter % L[i]
    return text.strip()

#4d
# antar det er snakk om beløper opp til 9 siffer
def add_words(string):
    w1 = text.split()
    for i in range(len(w1)):
        try:
            num = int(w1[i])
            w1[i] += '- ' + i_9txt(int(word))+' - '
        except:
            pass
    return ' '.join(w1)


        
