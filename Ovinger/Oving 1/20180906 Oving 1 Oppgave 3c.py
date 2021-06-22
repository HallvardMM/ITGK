#Øving 1 Oppgave 3c
import math
print("Har en sirkel med radius", 5.4, "som er grunnflate i en sylinder med høyde", 7.9)
Omkrets = round(math.tau * 5.4,1)
print("Omkrets av sirkelen:", Omkrets)  #tau er det samme som 2 pi
Areal_Sirkel = round(math.pi * 5.4**2,1)
print("Areal av sirkelen:", Areal_Sirkel)
print("Areal av sylinderen:", round(Omkrets * 7.9 + 2 * Areal_Sirkel,1))
