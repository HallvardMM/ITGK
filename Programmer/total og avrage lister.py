# total funksjoner
def total(liste): #tar inn en liste med tallverdier
    total=0
    for element in liste:
        total += element
    return total

def avreage(liste): #tar inn en liste med tallverdier
    avr=0
    for element in liste:
        avr += element
    return avr/len(liste)


def strlist_to_file(strlist):
    file = open('exampel.txt','w')
    for element in strlist:
        file.write(element + '\n')
    file.close()

def dump_pickle(verdi, file): #det du vil lagre
    import pickle
    output_file=open(file,'wb') #writebinært
    pickle.dump(verdi, output_file)
    output_file.close()

def gcd(tall1,tall2):
    if tall1 % tall2 == 0:
        return tall2
    else:
        return gcd(tall1, tall1 % tall2)


    

