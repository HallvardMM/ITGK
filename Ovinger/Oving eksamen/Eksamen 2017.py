#Eksamen 2017
#1a,2b,3a,4b,5c,6a,7c,8c,9b,10d,11d,12b,13b,14c,15a,16d,17b,18c,19b,20c


#2a
#feil på linje imid = (imin+imax) skulle stått imid = (imin+imax)//2

#2b
#[9,7,5,3,2,1] den endrer rekkefølgen på listen

#2c
#Den returnerer 101011001 som er binærtallet til 345.

#2d
#den stokker om tallene i listen eller randomiserer de

#3a
def file_to_table(filename):
    table=[]
    f=open(filename,'r')
    for line in f:
        line = line.strip()
        data = line.split(',')
        for i in range(6):
            data[i]=int(data[i])
        table.append(data)
    f.close()
    return table

#3b
"""def time_diff(start,end):
    if diff_date([start[:3],end[:3])==0:
        timer=end[3]-start[3]
        minutter=end[4]-start[4]
        sekunder=end[5]-start[5]
        return timer*60*60+minutter*60+sekunder
    elif diff_date([start[0],start[1],start[2]],[end[0],end[1],end[2]])==1:
        neste_dag=end[3]*60*60+end[4]*60+end[5]
        før_midnatt=24*60*60-(start[3]*60*60+start[4]*60+start[5])
        return før_midnatt+neste_dag
    else:
        return None #spesifiserers ikke i oppgaven, men dette er hvis samme bil kjører med mer enn 1 dag mellomrom"""

#3c
def check_min_distance(car_table,diff):
    crazydrivers=[]
    try:
        for i in range(len(car_table)):
            if (car_table[i][2:4]==car_table[i+1][2:4]) and (car_table[i+1][5]-car_table[1][5]<diff):
                crazydrivers.append(car_table[i+1][6])
    except IndexError:
        return crazydrivers
        

#3d
def liste_el_cars(car_table):
    el_cars=0
    for car in car_table:
        plate=car[6]
        if plate[:2]=="Ek" or plate[:2]=="El" or plate[:2]=="Ev":
            el_cars+=1
    return el_cars

#3e
def generate_license_numbers(amount):
    from random import randint
    plater=[]
    boks=['BS','CV','EL','FY','KU','LE','NB','PC','SY','WC']
    lengde=len(boks)
    for i in range(amount):
        plate=0
        while plate not in plater:
            plate=str(boks[randint(0,lengde-1)])+str(randint(10000,99999))
            plater.append(plate)
    return plater

print(generate_license_numbers(6))

#3f
def list_speeders(filename_a,filename_b,speed_limit,distance):
    time_limit=(Distance/speed_limit)*3600
    listestart = file_to_table(filename_a)
    listeslutt = file_to_table(filename_b)
    speeders=[]
    for bil_start in listestart:
        for bil_end in listeslutt:
            if bil_start[6]==bil_slutt[6]:
                tid = time_diff(bil_start[:6],bil_slutt[:6])
                if tid<time_limit:
                    speeders.append(bil_start[6])
    return speeders

#4a
def formatTime(seconds):
    time=seconds//3600
    minutt=(seconds % 3600)//60
    sec= seconds % 60
    if time < 10:
        hh = "0" + str(time)
    else:
        hh = str(time)
    if minutt < 10:
        mm = "0" + str(minutt)
    else:
        mm = str(minutt)
    if sec < 10:
        ss = "0"+str(sec)
    else:
        ss = str(sec)
    return hh+":"+mm+":"+ss

print(formatTime(12305))

#4a LF
def formater(time):
    if time < 10:
        return "0"+str(time)
    else:
        return str(time)

def formatTimeLF(seconds):
    timer = seconds//3600
    mins = (seconds%3600)//60
    sec = seconds%60
    streng = formater(timer)+":"formater(mins)+":"formater(sec)
    return streng

#4b
def valuesDecember():
    first=3*60*60+18*60
    period=12*60*60+25*60+12
    return first,period
#4c
def genTides():
    firstlow,period=valuesDecember()
    firsthigh=firstlow+firstlow/2
    secsindecember=31*24*3600
    lows=[]
    highs=[]
    for i in range(31*2):
        lav=firstlow+i*period
        høy=firsthigh+i*period
        if lav<secsindecember:
            lows.append(lav)
        if høy<secsindecember:
            highs.append(høy)
    return lows,highs

#4d
def genTidesStr(tideList):
    strenger=[]
    for element in tideList:
        dag=(element%24*3600)+1
        tidspunkt=element-dag*(24*3600)
        strenger.append(str(day)+" "+str(formatTime(item % (24*60*60))))
    return strenger
#4e
def checkTides(dayInMonth):
    lows,highs = genTides()
    secPerDay = 24*60*60 # 86400 seconds
    start_time = dayInMonth*secPerDay+9*(60*60) # 09:00 at dayInMonth
    end_time = start_time+4*(60*60) # 4 hours after 9:00 (13:00)
    for item in lows:
        if start_time <= item <= end_time:
            print('low tide at',formatTime(item % secPerDay))
            return
    for item in highs:
        if start_time <= item <= end_time:
            print('high tide at',formatTime(item % secPerDay))
            return
    print('no tides')

#4f
def listTides():
    lows, highs = genTides()
    secPerDay = 24*60*60 # 86400 seconds
    i = 0
    print('Day'.rjust(3),'First'.center(8),'Second'.center(8))
    for day in range(1,32): # days from 1 to 31 (including 31)
        line =str(day).rjust(3)
        while (i < len(lows)) and (lows[i] < day*secPerDay):
            line += ' '+ str(formatTime(lows[i] % secPerDay))
            i += 1
        print(line)
        



        
