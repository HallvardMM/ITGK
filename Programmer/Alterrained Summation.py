#Alternerede sum
n = int(input("n = "))
k = int(input("k = "))
y = 0
listen = []
summen = 0
i = 0
for x in range(1, n+1):
    y = x**2
    if x%2 == 0:
        y = y * (-1)
    summen = summen + y
    if summen > k:
        summen = summen - y
        break
    listen.append(y)
    i += 1
print(listen)
print(summen)
print("Den over er summen når den er mindre enn " + str(k) + " og den kom etter antall iterasjoner = " + str(i))
    
