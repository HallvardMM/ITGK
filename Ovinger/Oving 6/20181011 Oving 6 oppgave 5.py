#Øving 6 oppgave 5a
import random
def make_vec():
    y=[random.randint(-10,10),random.randint(-10,10),random.randint(-10,10)]
    return y

print(make_vec())

#Oppgave 5b

def vector_print(x,y):
    print(y,'=',x)

vector_print([1.20,4.50,4.40],'vec1')

#Oppgave 5c

def vec_skalar(liste,skalar):
    liste2=[]     
    for i in range(0, len(liste)):
        liste2.append(skalar * liste[i])
    return liste2

print(vec_skalar([1.2, 4.5, 4.4],4))

#Oppgave 5d

def vec_len(liste):
    y=0
    for i in range(0,len(liste)):
        y=y+(liste[i])**2
    z=y**(0.5)
    return z
    
vec1 = [1, 4, 3]
print(vec_len(vec1))

#Oppgave 5e

def vector_dot_product(vec1,vec2):
    y=0
    for i in range(0,len(vec1)):
        y=y+vec1[i]*vec2[i]
    return y

vec1 = [1, 4, 3]
vec2 = [2, 3.1, 5]
print("Prikkproduktet av",vec1,"og",vec2,"er:",format(vector_dot_product(vec1,vec2),".3f"))  

print("\n"*2)

#Oppgave 5f
def main():
    vector=make_vec()
    vector_print(vector,'vec1')
    skalar=float(input("Skriv inn en skalar "))
    ny_vector=vec_skalar(vector,skalar)
    print("Lengden før skalering er:",format(vec_len(vector),".2f"))
    print("Lengden før skalering er:",format(vec_len(ny_vector),".2f"))
    print("Forholdet mellom lengden før og etter skalering er",vec_len(ny_vector)/vec_len(vector))
    print("Prikkproduktet av",vector," og",ny_vector, "er:",vector_dot_product(vector,ny_vector))
main()
    
