#Øving 9 oppgave 2
#ai det skrives ut [88,92,100]
#aii det skrives ut 100

#b
fruit={}
fruit['eple']=2
fruit['pærer']=3
fruit['appelsinger']=1
print(fruit)

#c
fruit['bananer']=0
fruit['druer']=1
del fruit['eple']
del fruit['pærer']
del fruit['appelsinger']
print(fruit)

#d
for val in fruit.values():
    print(val)
#e
if 'bananer' in fruit:
    del fruit['bananer']
print(fruit)

#f
fruit['jordbær']=10
fruit['blåbær']=50
for key, value in fruit.items():
    print(key,value)
