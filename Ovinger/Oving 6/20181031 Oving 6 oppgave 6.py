# Øving 6 oppgave 6a

number_list=[i for i in range(100)]
print(number_list)

# Øving 6 oppgave 6b
summen = 0
for number in number_list:
    if number%3==0 or number%10==0:
        summen +=number

print(summen)

#Øving 6 oppgave 6c

for i in range(0,len(number_list)-1,2):
    number_list[i], number_list[i+1] = number_list[i+1],number_list[i]
print(number_list)

#Øving 6 oppgave 6d

reversed_list=[]
for i in range(len(number_list)):
    reversed_list.append(number_list[99-i])
    
print(reversed_list)
