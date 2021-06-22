#While
n=int(input("Tall: "))
while n>0:
    print(n)
    n=n-1

#Gjettespill
import random
# random.random() gir et tilfeldig flyttal mellom 0 og 1

#tall = random.randint(0,100) #Gir random tall mellom 0 og 100
#gjett = -1
#while(tall!=gjett):
#    gjett = int(input("Gjett hvilket tall mellom 1 og 100: "))
#    if (gjett>tall):
#        print("For høyt! ")
#    elif (gjett<tall):
#        print("For lavt! ")
#print("Riktig!")

# "for" variabel "in" [verdi1, verdi2, verdi3, osv]: (etterfulgt av kodelinjer)
#range(3) f.o.m "0" til men ikke med "3" == [0,1,2]
#range(fra,til,steg) range(1,6,2)==[1,3,5]
#telle nedover range(10,1,-3)

for n in range(3,31,3):
    print(n,"\t",n**2)

#x=x+4 kompaktform x+=4 denne formen gjelder for alle tegnene

#for t in range(24):
#    for m in range(60):
#        for s in range(60):
#            print(t,":",m,":",s)
            

for y in range(1,4):
    for x in range(1,4):
    z = x*y
    print(z)
        
