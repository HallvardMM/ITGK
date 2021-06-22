import random

def lang_liste(l):
    while len(l) != 40:
        l.append(random.randint(1, 100))
    return l

def bubble_sort(l):
    for j in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l

def selection_sort(liste):
    k = []
    f = len(liste)
    while len(k) != f:
        k.insert(0, 0)
        for j in range(len(liste)):
            if liste[j] != None and k[0] <= liste[j]:
                 k[0] = liste[j]
                 d = j
        liste.pop(d)
    return k
        
                   

while True:
    liste = lang_liste([])
    opg = str(input("opg? "))
    if opg == "a":
        print(bubble_sort(liste))
    elif opg == "b":
        print(selection_sort(liste))

