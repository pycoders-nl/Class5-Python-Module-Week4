"""Write a Python program to check the validity of a password (input from users)

Rules :

At least 1 letter between [a-z] and 1 letter between [A-Z]
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
If password is not valid throw ValueError with a proper error message
for each rule. If the password is valid print a success message. 
Use some from raise, except, assert, else and finally keywords."""


import re
p= input("Input your password :")
x = True
while x:  
    if (len(p)<6 or len(p)>16):
        raise ValueError ("Length has to be between 6-16 characters.")
    elif not re.search("[a-z]",p):
        raise ValueError('You have to  "$","#","@"')
    elif not re.search("[0-9]",p):
        raise ValueError("You should use at least one digit number.")
    elif not re.search("[A-Z]",p):
        raise ValueError("A capital letter must be used.")
    elif not re.search("[$#@]",p):
        raise ValueError("A symbol must be used.")
    
    else:
        print("Valid Password")
        x=False
        break

print("\n Your password is : ",p)
    