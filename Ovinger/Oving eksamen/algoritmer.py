def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
	
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
            #return found

def binærsøk(liste,element,start,slutt):
    midten=start+(slutt-start)//2
    if element==liste[midten]:
        return midten # her finner vi en tilfeldig indeks til listen
    
    elif slutt-start>1:
        if liste[midten]<element:
            return binærsøk(liste,element,midten+1,slutt)
        else:
            return binærsøk(liste,element,start,midten)
    else:
        return -1

def binærsøk_1_indeks(liste,element,start,slutt):
    midten=start+(slutt-start)//2
    if element==liste[midten]:
        return finn_første_indeks(liste,midten) # her finner vi første forekomst
    
    elif slutt-start>1:
        if liste[midten]<element:
            return binærsøk_1_indeks(liste,element,midten+1,slutt)
        else:
            return binærsøk_1_indeks(liste,element,start,midten)
    else:
        return -1

def finn_første_indeks(liste,indeks):
    while liste[indeks]==liste[indeks-1]:
        indeks-=1
    return indeks

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

def lønn_per_dag():
    while True:
        try:
            lønn=float(input("Hvor mye har du tjent? "))
            dager=int(input("Hvor mange dager har du jobbet? "))
            print("Du har tjent",lønn/dager,"kr per dag.")
        except ValueError as feilmelding:
            print(feilmelding)
            print("Du må skrive lønn som et flyttall")

        except ZeroDivisionError as feilmeld:
            print(feilmeld)
            print("Du kan ikke jobbe 0 dager")
        else:
            print("Takk for at du bruker programmet.")
        finally:
            mer=input("Vil du regne mer ja/nei?").lower().strip()
            if mer=='nei':
                break
lønn_per_dag()

        
        
            
    
