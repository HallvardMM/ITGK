#Slettet 6a) i forbifarten ;)

#Øving 1 oppgave 6b) 
r = int(5)
print("Vi har en sirkel med radius " + str(r))
omkrets = format(2 * 3.14 * r,'.2f')
print("Omkretsen er "+str(omkrets))
areal = format(3.14 * r ** 2,'.1f')
print("Arealet er "+str(areal))
h = int(8)
volum = float(float(areal) * int(h))
print("Sylinder med høyde "+str(h)+": Volumet er "+str(volum))
#Oppgave c)
oppgave=int(2*3.14*5)
print(str(oppgave))

#On most machines today, floats are approximated using a binary fraction with the numerator using the first 53 bits starting with the most significant bit and with the denominator as a power of two. In the case of 1/10, the binary fraction is 3602879701896397 / 2 ** 55 which is close to but not exactly equal to the true value of 1/10.

#Many users are not aware of the approximation because of the way values are displayed. Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine. On most machines, if Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display
