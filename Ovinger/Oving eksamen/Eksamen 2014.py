#Eksamen 2014
#1d,2b,3b,4d,5a,6b,7c,8c,9c,10d,11b,12d,13b(feil),14b,15a
#,16a,17a,18d,19c,20a,21b,22a,23a,24a,25a
#13a "… entydige, utførbare skritt som definerer en terminerende prosess" (unambiguous,executable steps that defines a terminating process).


#2a
def inputPerson():
    navn=input("Name: ")
    ID=input("ID: ")
    KG=int(input("KG: "))
    Size=int(input("Size: "))
    return [navn,ID,KG,Size]

#2b
def readDbFile(filename):
    output=[]
    f=open(filename,'r')
    for line in f:
        line=line.strip()
        liste=line.split(';')
        liste[2]=int(liste[2])
        liste[3]=int(liste[3])
        output.append(liste)
    f.close()
    return output
#2c
def printMemberList(db):
    print("NAMN"+" "*11+"ID-NR"+" "*4+"VEKT "+"kg. "+"SKJERMSTORLEIK")
    for i in range(len(db)):
        print(db[i][0]+" "*(15-len(db[i][0]))+db[i][1]+" "*(9-len(db[1][0]))+db[i][2]+" "*(5-len(db[i][2]))+"kg  "+db[i][3]+" "*(4-len(db[i][3]))+"KVADRATFOT")

#2d
def addPerson(filename):
    person=inputPerson()
    db = readDbFile(filename)
    db.append(person)
    f = open(filename,'a')
    s = person[0]+';'+person[1]+';'+str(person[2])+';'+str(person[3])+'\n'
    f.write(s)
    f.close()
    return db

#2e
def feet2seconds(feet):
    if feet > 4000:
        return 10 + (feet-4000)/200
    elif feet > 3000:
        return (feet-3000)/100
    else:
        return 0

#3a
def weatherStats(weatherData):
    print("There are",len(weatherData),"days in the period.")
    high=[]
    low=[]
    rain=[]
    for i in range(len(weatherData)):
        high.append(weatherdata[i][0])
        low.append(weatherdata[i][1])
        rain.append(weatherdata[i][2])
    warmest=max(high)
    coldest=min(low)
    rain=sum(rain)
    wday=high.index(warmest)+1
    cday=low.index(coldest)+1
    print("The highest temperature was",warmest,"C on day number",wday)
    print("The lowest temperature was",coldest," C on day number",cday)
    print("There was a total of",rain,"mm rain in the period")

#3b
def coldestThreeDays(weatherData):
    coldest=(weatherData[0][1]+weatherData[1][1]+weatherData[2][1])/3
    cday=1
    for i in range(1,len(weatherData)-2):
        averagetemp=(weatherData[i][1]+weatherData[i+1][1]+weatherData[i+2][1])/3
        if averagetemp<=coldest:
            cday=i+1
            coldest=averagetemp
    return cday

#3c
def addNewDay(extraData,weatherData):
    listen=string.split()
    maxtemp=float(listen[0][4:-1])
    mintemp=float(listen[0][4:-1])
    rain=float(listen[0][:-2])
    weahterData.append([mtemp,ltemp,rain])
    return weatherData

#4a
#returnerer 14
# tar å adderer  de ytterste i listen mulitplisert og fjerner de fra listen før den kjører seg selv rekursivt og legger sammen resultatet.

#4b
#lager et n*n sjakkmønster av 0 og 1.

#4c
#Den returnerer hver 3. bokstav i input ordet
# i dette filfelle ROSENBORG

#4d Må endre linje 10, 13 og 14:
# 10 if char != parentheses_list[-1]: 
# 13 parentheses_list.pop() # FIXED
# 14 return parentheses_list==[] # FIXED
#Forklaring:
#Line 10 sjekket ikke rekkefølge. Endret til å sjekke med parentes som ble sist lagt til lista.
#Linje 13 fjernet første forekomst av gitt parentes. Endret til å fjerne den som ble sist lagt til lista.
#Linje 14 returnerte det som var igjen av liste. Endret til å sjekke om lista var tom!
