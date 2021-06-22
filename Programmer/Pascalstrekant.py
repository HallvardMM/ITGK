#Øving 5 oppgave del a)
def Facu(n):
    y = 1
    for x in range(1, n+1):
        y = int(y * x)
    return y

def nChoosekk(n, k):
    y = int(Facu(n)/((Facu(k))*(Facu(n-k))))
    return y

def pascal(n):
    for x in range(0, n):
        for y in range(0, x+1):
            v = int(nChoosekk(x, y))
            print(v, end=" ")
        print()
            

