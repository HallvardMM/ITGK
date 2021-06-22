#Øving 3 Oppgave 4a)

#printer ut tallene 1,0,1,0,1,1,0,0,1 på formen 101011001
#som er binærkode for 345 viktig at binærkode leses fra høyre mot venstre

#345mod2=   1 
#345//2=172 fordi den runder ned
#172mod2=   0
#172//2=86
#86mod2=    0
#86//2=43
#43mod2=    1
#43//2=21
#21mod2=    1
#21//2=10
#10mod2=    0
#10//2=5
#5mod2=     1
#5//2=2
#2mod2=     0
#2//2=1
#1mod2=     1
#1//2=0 Her stopper den

#Vi ser da at hvis vi leser fra topp og ned tilsvarer det binærkode for 345
#fra høyre mot venstre

a=345
b=''
while a or b=='':
    b=str(a%2)+b
    a=a//2
print(b)

