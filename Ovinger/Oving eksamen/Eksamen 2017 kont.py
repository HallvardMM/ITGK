#Eksamen 2017 kont
#1c,2b,3a,4c,5d,6c,7a,8c,9a,10d,11d,12b,13c,14b,15a,16a,17c,18a,19d,20c

#2a
def file_to_list(filename):
    f=open(filename,'r')
    listen=[]
    for line in f:
        nylist=line.split('\t')
        nylist[2]=float(nylist[2])
        listen.append(nylist)
    f.close()
    return listen

#2b
def list_stores(dataList):
    butikk=[]
    for element in dataList:
        if element[0] not in butikk:
            butikk.append(element[0])
    return butikk
#2c
def sum_prices_stores(dataList,storeList):
    summen=[0]*len(storeList)
    for element in dataList:
        storeNr = storeList.index(element[0])
        summen[storeNr] += element[2]
    return summen

#2d
def rank_stores(storeList,sumStores):
    switch = True
    while(switch):
        switch = False
        for i in range(len(storeList-1)):
            if sumStores[i+1]<sumStores[i]:
                switch = True
                temp = sumStores[i]
                sumStores[i] = sumStores[i+1]
                sumStores[i+1] = temp
                temp = storeList[i]
                storeList[i] = storeList[i+1]
                storeList[i+1] = temp
    return storeList

#2e
def store_analysis(filename):
    dataList = file_to_list(filename)
    storeList = list_stores(dataList)
    sumStores = sum_prices_stores(dataList,storeList)
    print("The total price for shopping per store is:")
    for i in range(len(storeList)):
        print(storList[i],":",sumStores[i],"kr")
    print() #kunne også brukt "\n"
    rankList = rank_stores(storeList,sumStores)
    print("The ranking of stores according to prices is:")
    for i in range(len(ranklist)):
        print(i+1,ranklist[i])


#3a
def enter_line(prompt,lenght):
    streng=""
    while len(streng)!=lenght:
        streng=input(prompt)
        if len(streng)!=lenght:
            print("The text must be",length,"characters long")
    return streng

#3b
def adjust_string(text,lenght):
    if len(text)>lenght:
        text=text[:lenght]
        return text 
    elif len(text)<lenght:
        text=" "*((lenght-1)//2)+text
        text+=" "*(lenght-len(text))
    return text

#3c
def enter_line_smart(prompt,lenght):
    streng=input(prompt)
    streng=adjust_string(streng,lenght)
    return streng

#3d
def enter_show_text():
    content=[]
    for i in range(1,7):
        promt="Line "+str(i)+":"
        streng=enter_line_smart(prompt,30)
        content.append(streng)
    show_display(content)

#3e
def scroll_display(content,line):
    import time
    text = content[line-1] # Pick out the string to be scrolled
    for i in range(len(text)):
        text = text[1:]+text[0] # Text from index 1->end + text from index 0
        content[line-1]=text # insert scrolled text into context
        show_display(content) # show text on large display
        time.sleep(0.1) # wait for 0.1 seconds
#3f
def display_from_file(filename):
    import time
    f = open(filename)
    x = 0
    content=[]
    for line in f:
        line = adjust_string(line.strip(),30)
        content.append(line)
        x+=1
        if x==6:
            show_display(content)
            time.sleep(10)
            x=0
            content=[]
    f.close()

#4a
#Den returnerer "god middag!!"
#Den returenerer en streng der den tar første bokstav fra s1,s2,s3 så andre bokstav fra s1,s2,s3, osv.

#4b
#Den returnerer matrisen med de ytterste tallene byttet ut med 0

#m=[[0,0,0,0,0],
#   [0,3,4,5,0],
#   [0,4,5,6,0],
#   [0,5,6,7,0],
#   [0,0,0,0,0]]

#4c
#Den returnerer "The Matrix"
#Den tar inn en streng og returnerer en ny streng bestende av annenhver bokstav lest baklengs fra inputen

#4d
#2*2*4*16=256
#returnerer 
    
