# ## 4. The Greatest Common Divisor
# As a user, I want to use a program which can calculate the `greatest common divisor (GCD)` of my inputs. 

# Acceptance Criteria:
# - Ask user the enter the number of inputs (n).
# - Ask user to enter `n` input numbers one by one.
# - Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# - Calculate the greatest common divisor (GCD) of `n` numbers.
# - Use `gcd` function in module of math.
from math import gcd
n=input("n: ")
liste=[]
try:
    n=int(n)
    for i in range(n):
        liste.append(int(input("value: ")))
    g=liste[0]
    for i in range(len(liste)):
        g=gcd(g,liste[i])    
    print(g)
except (ValueError) as e:
    print('Error Code: ',e)