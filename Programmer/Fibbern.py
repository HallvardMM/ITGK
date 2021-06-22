# fibonaccitall
a = 0
b = 1
i = 0
summen = 0
ant = int(input("Antall fibonacci-tall: "))
fib = []
while i < ant:
    fib.append(a)
    i += 1
    summen += a
    if i < ant:
        fib.append(b)
        i += 1
        summen += b
    a = a + b
    b = b + a
print(fib)
print("Summen av fibtall til antall: ",summen)

