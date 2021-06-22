def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def day_check(day):
    if day == 0:
        return "man"
    elif day == 1:
        return "tir"
    elif day == 2:
        return "ons"
    elif day == 3:
        return "tor"
    elif day == 4:
        return "fre"
    elif day == 5:
        return "lor"
    elif day == 6:
        return "son"

def weekday_newyear(year):
    day = (year - 1900) % 7
    for y in range(1900, year):
        if is_leap_year(y):
            day += 1
    if day >= 7:
        day += -7
    return day

def is_workday(day):
    if day < 5:
        return True
    else:
        return False

def workdays_in_year(year):
    i = 0
    day = weekday_newyear(year)
    if is_leap_year(year):
        ant = 366
    else:
        ant = 365
    for y in range(0, ant):
        if day == 7:
            day = 0
        if is_workday(day):
            i += 1
        day += 1
    return i
                
    
while True:
    opg = input("Hvilken oppgave? ")
    
    if opg.lower() == "a":
        for year in range(1900, 1920):
            day = weekday_newyear(year)
            print(year, day_check(day))

    
    elif opg.lower() == "b":
        print(is_workday(2))
        print(is_workday(5))
    
    elif opg.lower() == "c":
        for year in range(1900, 1920):
            print(str(year) + " har " + str(workdays_in_year(year)) + " arbeidsdager")
