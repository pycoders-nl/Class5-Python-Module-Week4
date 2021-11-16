### As a user, I want to use a program which can calculate the greatest common divisor (GCD) of my inputs.

class FormulaError(Exception): 
    pass
import math

def entry(x,y):                                         # I tried to use 'Exceptions
    try:
        x = str or float
    except ValueError as ne:
        raise FormulaError(ne)
    else:
        y = str
        raise FormulaError("Please entry a number!")
    
x = int(input("Please entry a num for x: "))
y = int(input("Please entry a num for y: "))
def gcd(x,y):
    return math.gcd(x,y)
print(gcd(x,y))
#print(entry(x,y))