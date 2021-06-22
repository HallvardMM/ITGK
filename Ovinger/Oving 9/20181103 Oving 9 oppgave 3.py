#Øving 9 oppgave 3
#a
setten=set()
#b
for i in range(1,21,2):
    setten.add(i)
print(setten)

#c
setto=set()
for i in range(1,10,2):
    setto.add(i)
print(setto)

#d
settre=setten-setto
print(settre)

#e forventer et tomt set eller none
settfire=settre.intersection(setto)
print(settfire)
# fikk set()

#f
def allUnique(lst):
    if len(lst)==len(set(lst)):
        y=True
    else:
        y=False
    return y
print(allUnique([1,3,2,6,8]))
print(allUnique([1,3,5,2,3,7]))

#g
def removeDuplicates(lst):
    y=set(lst)
    x=list(y)
    return x
print(removeDuplicates([1,3,5,2,3,7]))




