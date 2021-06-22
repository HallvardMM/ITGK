#Øving 6 oppgave 8
#Oppgave a

def separate(numbers,threshold):
    less_then=[]
    moreorequal=[]
    for i in numbers:
        if i<threshold:
            less_then.append(i)
        else:
            moreorequal.append(i)
    return less_then, moreorequal

print(separate([1,2,3,4,5],3))
        
#Oppgave b

def multiplication_table(n):
    multi=[]
    for i in range(n):
        multi.append([])
    for i in range(n):
        for y in range(n):
            multi[i].append((i+1)*(y+1))
    return multi

print(multiplication_table(4))
            

