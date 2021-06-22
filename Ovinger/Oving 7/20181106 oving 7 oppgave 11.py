#øving 7 oppgave 11
#a
from random import randint

def randList(size, lower_bound, upper_bpund):
    liste=[]
    for i in range(size):
        liste.append(randint(lower_bound,upper_bpund))
    return liste

#b
def compareLists(list1, list2):
    liste=[]
    for ch in list1:
            if ch in list2 and ch not in liste:
                liste.append(ch)
    return liste

#C
def multiCompList(lists):
    common = compareLists(lists[0], lists[1])
    for r in range(2,len(lists)):
        common = compareLists(common, lists[r])
    return common
#D

def longestEven(liste):
    ant = 0
    tempAnt = 0
    index = 0
    tempIndex = 0
    tempEven = 0
    for i in range(len(liste)):
            if (liste[i] % 2 == 0):
                    if tempAnt == 0:
                            tempIndex = i
                    tempAnt +=1
                    tempEven +=1
            else:
                    if tempAnt > ant:
                            ant = tempAnt
                            index = tempIndex
                    tempAnt = 0
    if tempEven == len(liste):
        ant = len(liste)
    return index, ant

def main():
    print(randList(10,2,7))
    a = [1,2,3]
    b = [4,3,1]
    print(compareLists(a,b))
    c = [7,2,1]
    d = [a,b,c]
    print(multiCompList(d))
    liste = [4,3,3,6,2,6,8,3,4,3,3]
    print(longestEven(liste))
 
main()


            
    
        
        
