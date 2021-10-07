# Write a Python program to check the validity of a password (input from users)
### Rules :
### At least 1 letter between [a-z] and 1 letter between [A-Z]
### At least 1 number between [0-9].
### At least 1 character from [$#@].
### Minimum length 6 characters.
### Maximum length 16 characters. 

class FormulaError(Exception):  
    pass
import string                                                                      # I tried to use some 'Modelus'
import stdiomask

def password(passwordd):                                                           # I tried to use 'Exceptions'
    lengt = len(passwordd).split
    if len(lengt) < 6 and len(lengt) > 16:
        raise FormulaError("You should entry between 6 and 16 charachters!")
    try: 
        pass_cont = list(string.ascii_letters + string.digits + string.punctuation)
        passwordd = pass_cont
    except ValueError as ve:
        raise FormulaError(ve)
    finally:
        print('This is always executed')

while True:
    passwordd = str(stdiomask.getpass(prompt="Please set a password!: ", mask="S"))    # I used 'stdiomask' modelu.
    if passwordd == "0":
        break
print(password())