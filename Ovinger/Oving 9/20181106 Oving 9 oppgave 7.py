    #Øving 9 oppgave 7
#a
def number_of_lines(filename):
    f = open(filename, "r")
    innhold = f.readlines()
    return innhold
    

print(len(number_of_lines("numbers.txt")))#len fordi da får vi 36 ikke alle tallene

#b
def number_frequency(filename):
    a = number_of_lines(filename)
    b = []
    for i in a:
        b.append(int(i.strip()))
    c={}
    for i in range(min(b), max(b)):
        count = 0
        for j in b:
            if j == i:
                count += 1
                c[i] = count
    return c

print(number_frequency("numbers.txt"))

#c

def pen(filename):
    a = number_frequency(filename)
    for key,value in a.items():
        print(str(key) + ":" + str(value))

pen("numbers.txt")


    
