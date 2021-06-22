#øving 7 oppgave 6
#a
from random import randint

random_numbers=[]
for i in range(101):
    random_numbers.append(randint(1,10))

print(random_numbers)

#b
print("Number of 2s:",random_numbers.count(2))

#c
print("Sum of numbers:",sum(random_numbers))

#d
random_numbers.sort()
print("Numbers sorted:",random_numbers)

#e
def most_common(lst):
    return max(set(lst), key=lst.count)
print("There are most of number:",most_common(random_numbers))

#f
random_numbers.reverse()
print("Numbers reversed:",random_numbers)



