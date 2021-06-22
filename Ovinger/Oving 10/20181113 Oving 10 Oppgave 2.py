#Øving 10 oppgave 2 Eksamen 2012
#2a
def summerOlympic(firstyear,lastyear):
    listen=[]
    for i in range(firstyear,lastyear+1):
        if i%4==0: #sjekket at 1948%4=0
            listen.append(i)
    return listen

#2b
def findAge(bYear,bMonth,bDay):
    (x,y,z)=(2018,11,13)
    if y<bMonth:
       return x-bYear-1
    elif y==bMonth:
        if z<bDay:
            return x-bYear-1
        else:
            return x-bYear
    else:
       return x-bYear

"""def find_Age(bYear,bMonth,bDay):
    (x,y,z)=current_date()
    år=x-bYear
    månde=y-bMonth
    dag=z-bDay
    if månde<0:
        return år-1
    elif månde==0:
        if dag<0:
            return år-1
    return år  """        

#2c
def printAgeDiff(table):
    try:
        for i in range(len(table)):
            if findAge(table[i][2],table[i][3],table[i][4]) > findAge(table[i+1][2],table[i+1][3],table[i+1][4]):
                print (table[i][0],table[i][1],"is older than",table[i+1][0],table[i+1][1])
                
            elif findAge(table[i][2],table[i][3],table[i][4])==findAge(table[i+1][2],table[i+1][3],table[i+1][4]):
                print (table[i][0],table[i][1],"is at the same age as",table[i+1][0],table[i+1][1])

            elif findAge(table[i][2],table[i][3],table[i][4])<findAge(table[i+1][2],table[i+1][3],table[i+1][4]):
                print (table[i][0],table[i][1],"is younger than",table[i+1][0],table[i+1][1])

    except IndexError:
        None
        
table=[['Justin','Bieber',1994,3,1],['Donald','Duck',1934,8,1],['George','Clooney',1961,5,6],['Eddie','Murphy',1961,4,3]]
printAgeDiff(table)     
    
#3a
def fu1(a): #starter med 1234
    r = 0
    while(a>0):
        s = a%10 #blir 4,3,2,1
        r = r + s #for hver iterasjon +4(4)+3(7)+2(9)+1(10)
        a = (a-s)/10 #blir 123,12,1,(0 og stopper)
    return r

print(fu1(1234)) # vil printe 10 noe den gjør...

#3b
def fu2(input):
    r = 0
    s = 0
    t = 0
    u = 0
    n = len(input) #20
    for c in input:
        if(c.isalpha()): #sjekker for bokstav
            r = r + 1 #15
        elif(c.isdigit()): #sjekker for tall
            s = s + 1 #0
        elif(c==' '): #sjekker for mellomrom
            t = t + 1 #4
        else: #sjekker for tegn
            u = u + 1 #1
    r = 100*r/n #15*100/20=75
    s = 100*s/n #0/20
    t = 100*t/n #4*100/20=20
    u = 100*u/n #100/20=5
    return(r,s,t,u) #output(75,0,20,5)

print(fu2("Ut pa tur, aldri sur"))

#3c
def fu3(a):
    if(a<=2):
        r = 1 #1.5625
    else:
        r = 1 + fu3(a/2) #100,50,25,12.5,6.25,3.125
    return r #1+1+1+1+1+1+1

print(fu3(100)) #printer 7

#4a
def cold_days(templist):
    i=0
    for element in templist:
        if element<0:
            i+=1
    return i
days = cold_days([1,-5,3,0,-6,-3,15,0])

#4b
def cap_data(array,min_value,max_value):
    for i in range(len(array)-1):
        if array[i]>max_value:
            array[i]=max_value
        elif array[i]<min_value:
            array[i]=min_value
    return array

A=[-70,30,0,90,23,-12,95,12]
result = cap_data(A,-50,50)

#4c
def generate_testdata(N,min_value,max_value):
    result=[]
    from random import randint
    for i in range(N):
        y=randint(min_value,max_value)
        if y not in result:
            result.append(y)
    return result

result2 = generate_testdata(10,-5,10)

#4d
def create_db(temp, rain, humidity, wind):
    weather={}
    for i in range(len(temp)):
        weather[i+1]=[temp[i],rain[i],humidity[i],wind[i]]
    return weather

temp = [1,5,3]
rain = [0,30,120]
humidity = [30,50,65]
wind = [3,5,7]
weather = create_db(temp,rain,humidity,wind)

#4e
def print_db(weather):
    print("Day | Temp | rain | humidity | wind")
    print("====+======+======+==========+======")
    for i in range(len(weather)):
        print(str(i).rjust(4), str(weather[i+1][0]).rjust(6),str(weather[i+1][1]).rjust(6),str(weather[i+1][2]).rjust(10),str(weather[i+1][3]).rjust(6))

print_db(weather) #Glemte å gjøre de til string


#4f
def strange_weather(temp,rain):
    antall_dager=len(temp)
    liste=[]
    for i in range(antall_dager-1):
        if temp[i]>temp[i+1] and rain[i]<rain[i+1]:
            liste.append(i+1)
    if len(liste)==0:
        return(0,0)
    else:
        for i in range(len(liste)-1):
            if not liste[i]+1==liste[i+1]:
                liste.pop(liste[i])
        return(liste[0],liste[0]+len(liste))

temp=[1,3, 4,-5,-6,-7,-8,-9,3,0]
rain=[0,20,30,0,10,30,50,0,5,2]
(start, stop) = strange_weather(temp,rain)


    
