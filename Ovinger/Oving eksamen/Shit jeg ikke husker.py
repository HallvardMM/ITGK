#Alt jeg ikke husker
import algoritmer

lønn_per_dag()

print(abs(-12))
print(round(1234,-3))

print("Yo I'm a big boy".rjust(40),end="")
print("I walk on water".ljust(40),"\n")
print("\tk") #tab er lik 8 mellomrom 
print(" "*8+"k")


print(ord(chr(ord('A'))))
print(ord(chr(ord('a'))))


print("Hei".upper())
print("Skjer".lower())


while True:
    break

def alle_untatt_5(liste):
    while len(liste)>0:
        for element in liste:
            if element != 5:
                print(element, end=" ")
            else:
                continue
        break

alle_untatt_5([1,2,3,4,5,6,7,8,9])

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
print(fac(7))



def nchoose(n,k):
    return fac(n)/(fac(k)*fac(n-k))

def pascal(n):
    for i in range(n):
        for y in range(i+1):
            print(str(int(nchoose(i,y))).rjust(3),end=" ")
        print()

pascal(4)



print(pow(6,3))
for i in range(100):
    print(chr(i), end=" ")


def pickle_my_bum(filename):
    import pickle 
    file=open(filename,'wb')
    inputtet=input("Skriv det du vil pickle: ")
    pickle.dump(inputtet,file)
    file.close()
    return True

def unpickle_my_bum(filename):
    import pickle
    file = open(filename,'rb')
    teksten=pickle.load(file)
    file.close()
    return teksten




pickle_my_bum("Test.txt")
print(unpickle_my_bum("Test.txt"))

dicti={'Arne':9415438234, 'Kåre':932472354}
del dicti['Arne']
dicti['Jens']=953214798324
print(dicti)
