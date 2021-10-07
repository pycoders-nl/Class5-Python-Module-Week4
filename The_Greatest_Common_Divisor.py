'''## 4. The Greatest Common Divisor
As a user, I want to use a program which can calculate the `greatest common divisor (GCD)` of my inputs. 

Acceptance Criteria:
- Ask user the enter the number of inputs (n).
- Ask user to enter `n` input numbers one by one.
- Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
- Calculate the greatest common divisor (GCD) of `n` numbers.
- Use `gcd` function in module of math.
'''

import math
def commond():
    liste = []
    try:
        number =int(input("number of inputs: ")) #Ask user the enter the number of inputs (n).

    except Exception:
        print("de not enter Nan or non numerical inputs")

    else:
        for i in range(number):
            j = int(input("enter the number :")) #Ask user to enter `n` input numbers one by one
            liste.append(j)
    return print(math.gcd(*liste)) #Calculate the greatest common divisor (GCD) of `n` numbers
commond()
    
