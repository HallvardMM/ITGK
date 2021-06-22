# 2015 eksamen
# 1b,2b,3c,4d,5b,6a,7c,8a,9b,10c,11b,12d,13a,14c,15b,16a,17a,18d,19a,20a
# alt riktig!
# 2a printer julenissen tar annenhver bokstav fra hvert ord.

# 2b printer 64
# Multipliserer x med x ganger med 2 til x blir over 10

#3a
def readTime():
    hour=0
    minutt=0
    sek=0
    while not hour:
        hour=int(input("Enter hour: "))
        if not ((hour>=0)and(hour<23)):
            print("- ERROR: Hour must be between 0 and 23!")
            hour=False
    while not minutt:
        minutt=int(input("Enter minutt: "))
        if not ((minutt>=0)and(minutt<59)):
            print("- ERROR: Minute must be between 0 and 59!")
            minutt=False
    while not sek:
        sek=int(input("Enter sek: "))
        if not ((sek>=0)and(sek<59)):
            print("- ERROR: Second must be between 0 and 59!")
            sek=False
    return [hour,minutt,sek]

#3b
def convertTime(time,mode):
    if mode=='time':
        hour=time//3600
        minutt=(time-(hour*3600))//60
        sek=(time-hour*3600-minutt*60)
        return[hour,minutt,sek]
    elif mode=='sec':
        return (3600*time[0]+60*time[1]+time[2])

#3c
def travelTime():
    print("Give departure time in hour, minute and second: ")
    dep=readTime()
    print("Give arrival time in hour, minute and second: ")
    arriv=readTime()
        while sum(dep)>sum(arriv):
            print("- ERROR: Arrival time must be later than Departure time")
            arriv=readTime()
    dep=convertTime(dep,'sec')
    arriv=convertTime(arriv,'sec')
    tid=convertTime(arriv-dep,'time')
    print("Traveltime: ",tid[0],"hours,",tid[1],"min",tid[2],"sec")

#3d
def busTime(BusRoute):
    return convertTime(BusRoute[3:5]+[0],'sec')-convertTime(BusRoute[1:3]+[0],'sec')
    
def analyzeBusRoutes(BusTables):
    slowestTimeSec = fastestTimeSec = busTime(BusTables[0])
    slowestBus = fastestBus = BusTables[0][0]
    for BusRoute in BusTables:
        if busTime(BusRoute) > slowestTimeSec:
            slowestTimeSec = busTime(BusRoute)
            slowestBus = BusRoute[0]
        elif busTime(BusRoute) < fastestTimeSec:
            fastestTimeSec = busTime(BusRoute)
            fastestBus = BusRoute[0]
            slowestTime = convertTime(slowestTimeSec,'time')
            fastestTime = convertTime(fastestTimeSec,'time')
            print("The slowest bus route is bus nr.",slowestBus,'and it takes',slowestTime[0],'hour, ',slowestTime[1],'min.')
            print("The fastest bus route is bus nr.",fastestBus,'and it takes',fastestTime[0],'hour, ',fastestTime[1],'min.')


#4a
NTNU_scores = (89,77,65,53,41,0)
NTNU_letters = ('A','B','C','D','E','F')
TASKS = ('1','2a','2b','2c','3a','3b','3c','3d','4a','4b','4c','4d','4e','4f','4g','4h')
WEIGHTS = tuple([25]+(15*[5]))

#4b
def makeArrayI(Numbers,Texts):
    liste=[]
    for i in range(len(Numbers)):
        liste.append([numbers[i],Texts[i]])
    return liste

#4c
def computeScore(Points,WEIGHTS):
    poeng=0
    maxpoeng=0
    for i in range(len(points)):
        maxpoeng+=10*WEIGHTS[i]
    for y in range(len(points)):
        poeng+=points[y]*WEIGHTS[i]
    return poeng/maxpoeng*100
#4d
def score2letter(scoreSum,LimitLetters):
    for element in LimitLetters:
        if element[0]<scoreSum:
            return element[1]
#4e
def addCandidate(candidateNumber,Scores,WEIGHTS):
    tekst=str(candidateNumber)+" "
    poeng=computeScore(Scores,WEIGHTS)
    for element in Scores:
        tekst+=str(element)+"\t"
    try:
        tekst=tekst+str(round(poeng,1))+"\n"
        f=open('eksamen.txt','a')
        f.write(tekst)
    except:
        print("[Errno 2] No such file or directory: 'eksamen.txt'")
    finally:
        f.close()

#4f
def nummarizeTable(Table):
    for i in range(len(Table)):
        if (i<len(Table)-1):
            Table[i]=int(Table[i])
        else:
            Table[i]=float(Table[i])
        return Table

def readResultFile(filename):
    listen=[]
    f=open(filename,"r")
    for line in f:
        line=line.strip()
        y=line.split()
        y=nummarizeTable(y)
        listen.append(y)
    f.close()
    return listen

#4g
def checkResultOK(filename, WEIGHTS):
    allOK = True
    results = readResultFile(filename)
    count={}
    for line in results:
        if(max(line[1:-1])>10 or min(line[1:-1])<0):
            print("ERROR: Candidate",line[0],"scores are not between 0-10!")
            allOK = False
        if line[-1]!=computeScore(line[1:-1],WEIGHTS):
            print("ERROR: Candidate",line[0],"has wrong total score!")
            allOK = False
            count[line[0]]=count.get(line[0],0) +1
            for key in count:
                if count[key]>1:
                print("ERROR: Candidate",key,"appears more than once!")
                allOK = False
    return allOK
            
#4h
def listAll(filename,limitLetters):
    results = readResultFile(filename)
    results.sort() # Sorterer etter kandidatnr
    count = 0
    for line in results:
        grade = score2Letter(line[-1], limitLetters)
        print(str(line[0]),str(round(line[-1],1)).rjust(5),grade)
        count+=1
    return count
        
        
    
    
    
