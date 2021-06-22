import math
import cmath #mattafunksjoner for komplekse tall

def root(x):
    if x >= 0:
        svar=math.sqrt(x)
    else:
        svar=cmath.sqrt(x)
    return svar

def main():
    while input ("fortsett: f ; Slutt: s ") == "f":
        tall = float(input("Tall: "))
        print("Roten er", root(tall))
main()

