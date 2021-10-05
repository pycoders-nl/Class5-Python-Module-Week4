"""## 4. The Greatest Common Divisor
As a user, I want to use a program which can calculate the `greatest common divisor (GCD)` of my inputs. 

Acceptance Criteria:
- Ask user the enter the number of inputs (n).
- Ask user to enter `n` input numbers one by one.
- Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
- Calculate the greatest common divisor (GCD) of `n` numbers.
- Use `gcd` function in module of math.
"""
import math

numberofnumbers = int(input("How many number you want to enter : "))
numberoflist = list()
while numberofnumbers > 0 : 
    try :
        numbers = int(input("Enter numbers one by one : "))
    except ValueError : 
        print("Invalid type . Write A Valid number")
    else : 
        numberoflist.append(numbers)
        numberofnumbers -= 1
print(math.gcd(*numberoflist))