#Øving 10 oppgave 1
#a
def recursive_sum(n):
    if n == 0:
        return 0
    return n+recursive_sum(n-1)

print(recursive_sum(53)) #gir 1431

#b
def fac(n):
    if n == 0: #dette for tilfelle fac(0)
        return 1
    return n*fac(n-1)
print(fac(5)) #gir 120
print(fac(3)) #gir 6

#c
def find_smallest_element(numbers): #ikke rekusjon
    y=0
    for elements in numbers:
        y+=elements
        try:
            for n in range(len(numbers)):
                if numbers[n]<numbers[n+1]and numbers[n]<y:
                    y=numbers[n]
        except IndexError:
            if numbers[n]<y:
                y=numbers[n]
        return y
        


print(find_smallest_element([6,2,3,4,5,1]))

#d 

def binary_search(numbers, element):
    index = len(numbers)//2-1
    end = int(len(numbers)) - 1
    while numbers[index] != element:
        if index == end:
            return (-float('inf'))
        elif numbers[index] > element:
            end = index
            index = int(index/2)
        elif numbers[index] < element:
            index = int((index+1 + end)/2)
    return index
        
print(binary_search([1,4,6,9,13,34,45,53,65,78],53))


#d stjerne: worst case vil den bruke O(log n)

#e
import time
from turtle import *
 
pensize(2)
pencolor("orange")
bgcolor("green")
fillcolor("blue")
hideturtle()
speed(1000)
 
def halfPetal():
    forward(50)
    left(30)
    forward(75)
    left(30)
    forward(50)
    left(120)
 
def petal():
    for i in range(2):
        halfPetal()
     
def flower(num, i=1):
    if num==0:
        return
    if i==1:
        begin_fill()
    for y in range(num): #Ikke rekusjon 
        petal()
        left(360/num)
    if i==i:
        end_fill()

flower(12)
time.sleep(5)
