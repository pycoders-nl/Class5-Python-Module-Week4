"""## 1. Password
Write a Python program to check the validity of a password (input from users)
    
**Rules :**
- At least 1 letter between [a-z] and 1 letter between [A-Z]
- At least 1 number between [0-9].
- At least 1 character from [$#@].
- Minimum length 6 characters.
- Maximum length 16 characters.

If password is not valid throw `ValueError` with a proper error message for each rule.
If the password is valid print a success message. Use some from  `raise`, `except`, `assert`, `else` and `finally` keywords.
"""

import string
def checkvalueerror(password):
    """
    This function check every conditions for password.
    """
    if len(password)<6 or len(password)>16 : #checked min and max character
        raise ValueError ("Password has to between 6-16 characters.")
    elif len({"$","#","@"} & set(password)) == 0:#special characters checked
        raise ValueError('You should use "$","#","@"')
    elif len(set(string.digits) & set(password)) == 0 : #checked any digit inside of password , string.digits gives us between 1-9 digits
        raise ValueError ("You have to use at lease number between 1-9")
    assert not(len(set(string.ascii_lowercase) & set(password)) == 0 or len(set(string.ascii_uppercase) & set(password)) == 0) # checked upper and lower letters string.ascii gives us all lower and upper letters


while True : 
    password = input("Write a password : ")
    try : 
        checkvalueerror(password)
    except ValueError as V : 
        print(V)
    except AssertionError : 
        print("You have to use at least 1 letter between [a-z] and 1 letter between [A-Z]")
    else : 
        print("Successful Password.")
    finally:
        print("Better than 'password'")