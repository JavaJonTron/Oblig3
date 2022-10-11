import operator

modulo=operator.mod


def isLeapYear(year):
    if (modulo(year, 4)==0 and modulo(year, 100) !=0 or modulo(year, 400) == 0):
        print("The year is a leap year!")
        return True
    elif (modulo(year, 4)!=0 and modulo(year, 100) ==0 or modulo(year, 400) != 0):
        print("The year isn't a leap year!")
        return False
