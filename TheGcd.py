"""As a user, I want to use a program which can calculate the greatest common divisor (GCD) of my inputs.

Acceptance Criteria:

Ask user the enter the number of inputs (n).
Ask user to enter n input numbers one by one.
Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
Calculate the greatest common divisor (GCD) of n numbers.
Use gcd function in module of math."""


import math
def TheGCD():
  i=0
  
  n = int(input("Enter number of elements : "))
  lst=[]
  if n<0:
     raise ValueError("Number of elements must be higher than zero") 
  else:
     while i<n : 
       
       try :
           
         numbers=int(input("Press ↵ after each number : "))
       except ValueError : 
         print("Enter valid integer numbers.")
         a=input(f"Enter Q for quit,\nPress'C' for continue and enter {n-i} numbers to complete :")
         if a=="Q":
            break
         elif a=="C":
            continue
         
       else : 
         lst.append(numbers)
         i += 1
  return print(f"TheGCD of {len(lst)} number(s) :",math.gcd(*lst))
TheGCD()