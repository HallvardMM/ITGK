#Eksamen 2013
#1d,2b,3d,4a,5b,6b,7a,8c,9b,10c,11c,12c,13b,14b,15c,16d,17b,18b,19d,20c
#10c rundt 100 instruksjonen er vanlig datamaskin
#15c nettverks pålitlighet uavbrutt/kontinuerlig
#4 feil

#2a
def yatzy(t1,t2,t3,t4,t5):
    liste=[t1,t2,t3,t4,5].sort()
    if liste[0]<1:
        print("Ikke bruk input mindre enn 1!")
    elif liste[-1]>6:
        print("Ikke bruk input stoerre enn 6!")
    else:
        return liste
#2b
def maxi_yatzy(liste):
    flestverdi=0
    maxantall=0
    
    for i in range(1,7):
        antall = 0
        for item in liste:
            if (item==i):
                antall+=1
        if antall >= maxantall:
            flestverdi = i
            maxantall = antall
    melding="Du kastet "+str(len(liste))+" terninger og fikk flest "
    melding= melding+str(flestverdi)+" ("+str(maxantall)+"like)."
    return melding

#3a
# den sorterer listen slik at den blir [10,8,8,5,4,2,1,1]

#3b
#returnerer 8 antall siffer  i tallet x.

#4a
def enterWords():
    wordList=[]
    inputen="x"
    while inputen!="":
        inputen=input("Enter word [Press Enter to quit]: ")
        if inputen !="":
            wordList.append(inputen)
    return wordList

#4b
def noVowels(inList):
    vowels=['a','e','i','o','u','y']
    outList=[]
    for string in inList:
        s=""
        for ch in string:
            if ch not in vowels:
                s+=ch
        outList.append(s)
    return outList

print(noVowels(['house','chair','cat']))

#4c
from random import randint
def randomSequence(listOne,listTwo):
    if len(listOne)>len(listTwo): #Sjekker hvilken liste som er lengst
        y=len(listTwo) # sto ikke i teksten om de må være like lange
    else:
        y=len(listOne)
    for i in range(y):
        x=randint(0,y-1)
        temp1=listOne[i]
        temp2=listTwo[i]
        listOne[i]=listOne[x]
        listTwo[i]=listTwo[x]
        listOne[x]=temp1
        listTwo[x]=temp2
    newlistOne=listOne
    newlistTwo=listTwo
    return (newlistOne,newlistTwo)

print(randomSequence(['house','chair','cat'],['Ape','bil','piano']))


#4d
def printNewlines(number):
    print("\n"*(number-1))

#4e
def playGame(answers,puzzles):
    poeng=0
    for i in range(len(puzzles)):
        print("Puzzle word:",puzzles[i])
        question=input("Guess word? ")
        if question==answers[i]:
            print("You answered correctly!")
            poeng+=1
        else:
            print("You answered incorrectly! the answer should be",answers[i])
    return poeng

#4f
print("The NoVowels Game\n"+"="*35+"\nPlayer 2: Look away from the screen\nPlayer 1: Write in a list of English words in lower-case.")
wordList=enterWords()
noVowelsList=noVowels(wordList)
(answers,quizzes)=randomSequence(wordList,noVowelsList)
printNewlines(50)
print("Player 2: Guess words that lack all vowels:")
points=playGame(answers,quizzes)
print("You got "+str(points)+" of "+str(len(answers))+" points.")


    
