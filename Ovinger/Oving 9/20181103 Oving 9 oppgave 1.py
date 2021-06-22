#Øving 9 oppgave 1
#a
my_family={}

#b
def add_family_member(x,y):
    my_family[x]=y

#add_family_member('bror', 'Arne')
#print (my_family)
#add_family_member('far', 'Bob Bernt')
#print (my_family)

#c
def add_family_member2(x,y):
    if x in my_family:
        z=my_family[x]
        z.append(y)
    else:
        my_family[x]=[y]

add_family_member2('bror', 'Arne')
add_family_member2('mor', 'Anne')
add_family_member2('bror', 'Geir')

print(my_family)

#d
for key, value in my_family.items():
    print(key,value)
