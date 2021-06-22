from random import *

def blackjack():
    k1 = randint(1, 11)
    k2 = randint(1, 11)
    d1 = randint(1, 11)
    d2 = randint(1, 11)
    print("Dealers cards are " + str(d1) + " and ?")
    if k1 == 11:
        a = int(input("Do you want ace to be 1 or 11? "))
        if a == 1:
            k1 = 1
        else:
            a == 11
    elif k2 == 11:
        a = int(input("Do you want ace to be 1 or 11? "))
        if a == 1:
            k2 = 1
        else:
            a == 11
    x = k1 + k2
    if x == 21:
        print("Blackjack! $$$$$")
    while x < 21:
        print("Your score is: " + str(x))
        b = input("Do you want another card? (J/N) ")
        if b == "J":
            n = randint(1, 11)
            if n == 11 and not a:
                a = int(input("Do you want ace to be 1 or 11? "))
                if a == 1:
                    n = 1
            elif n == 11 and a == 1:
                n = 1
            x += n
        elif b == "N":
            print("Your score is: " + str(x))
            break
    if x <= 21 and x > (d1 + d2):
        print("Dealers score is: " + str(d1 + d2))
        print("You won!")
    elif x > 21:
        print("You got " + str(x))
        print("Dealers score is: " + str(d1 + d2))
        print("You lost")
    elif x == (d1 + d2):
        print("Dealers score is: " + str(d1 + d2))
        print("Better luck next time, the dealer is the devil")
        print("You lost")
    else:
        print("Dealers score is: " + str(d1 + d2))
        print("You lost")
              

while True:
    print("Welcome to blackjack!")
    print()
    blackjack()
    print()
