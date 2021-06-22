def sammenligning(x, y):
    liste_x = list(x)
    liste_y = list(y)
    liste_t = []
    for i in range(len(y)-1):
        if liste_y[i].lower() == liste_x[0].lower() and liste_y[i+1].lower() == liste_x[1].lower():
            liste_t.append(i)
    return liste_t

str1 = "iS"
str2 = "Is this the real life? Is this just fantasy"
str1 = "oo"
str2 = "Never let you go let me go. Never let me go ooo"


print(sammenligning(str1, str2))

str1 = "oo"
str2 = "Never let you goooo let me goo. Never let me goo oooo"
str3 = "cool"

def endring(x, y, z):
    liste_x = list(x)
    liste_y = list(y)
    liste_t = list(y)
    for i in range(len(y)-1):
        if liste_y[i].lower() == liste_x[0].lower() and liste_y[i+1].lower() == liste_x[1].lower():
            liste_t[i] = z
            liste_t[i+1] = ""
    liste_t = "".join(liste_t)
    return liste_t

print(endring(str1, str2, str3))
