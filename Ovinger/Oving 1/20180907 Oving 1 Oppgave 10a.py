#Øving 1 oppgave 10a)
from math import sqrt
h = float(input("Høyde "))
areal = float(sqrt(3)*((3/sqrt(6))*h)**2)
print("Et tetraeder med høyde "+str(h)+" har areal "+str(areal))
#Øving 1 oppgave 10b)
volum =float(sqrt(2)*((3/sqrt(6))*h)**3/12)
print("Et tetraeder med høyde "+str(h)+" har volum "+str(volum))
#Øving 1 oppgave 10c)
print("Et tetraeder med høyde "+str(h)+" har volum "+str(volum)+" og areal "+str(areal)+".")
