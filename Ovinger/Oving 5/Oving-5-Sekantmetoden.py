from math import *

def f(x):
    return (x - 12) * e**(x/2) - 8 * (x + 2)**2

def g(x):
    return -x - 2 * x**2 - 5 * x**3 + 6 * x**4

def differentiate(x1, x0, func):
    i = 0
    if func == "f":
        i = (f(x1) - f(x0)) / (x1 - x0)
    elif func == "g":
        i = (g(x1) - g(x0)) / (x1 - x0)
    return i

def secant_method(x0, x1, func, tol):
    if func == "f":
        while abs(x1 - x0) > tol:
            y = differentiate(x1, x0, "f")
            i = x1 - (f(x1) / y)
            x0 = x1
            x1 = i
        return x1, f(x1)
    elif func == "g":
        while abs(x1 - x0) > tol:
            y = differentiate(x1, x0, "g")
            i = x1 - (g(x1)/y)
            x0 = x1
            x1 = i
        return x1, g(x1)

while True:
    opg = input("Hvilken oppgave? ")

    if opg.lower() == "a":
        
        print(f(0))
        print(g(1))

    elif opg.lower() == "b":
        i = 0
        x1 = float(input("Tall 1: "))
        x0 = float(input("Tall 2: "))
        func = input("f eller g: ")
        print("derivative: ", differentiate(x1, x0, func))

    elif opg.lower() == "c":
        i = 0
        x0 = float(input("Tall 1: "))
        x1 = float(input("Tall 2: "))
        func = input("f eller g: ")
        tol = float(input("Toleransegrensen? "))
        a, b = secant_method(x0, x1, func, tol)
        if b != 0:
            b = format(b, ".2e")
        else:
            b = round(b, 2)
        print("Funksjonen nærmer seg et nullpunkt når x = " + str(round(a, 2)) + " , da er f(x) = " + str(b))
