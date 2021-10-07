'''
## 1. Password
Write a Python program to check the validity of a password (input from users)
*Rules :**
- At least 1 letter between [a-z] and 1 letter between [A-Z]
- At least 1 number between [0-9].
- At least 1 character from [$#@].
- Minimum length 6 characters.
- Maximum length 16 characters.
If password is not valid throw `ValueError` with a proper error message for each rule.
If the password is valid print a success message. Use some from  `raise`, `except`, `assert`, `else` and `finally` keywords.
'''


import re

control1="^.*(?=.*[a-z]).*$"
control2="^.*(?=.*[A-Z]).*$"
control3="^.*(?=.*[0-9]).*$"
control4="^.*(?=.*[$#@]).*$"
control5="^.*(?=.{6,16}).*$"

def password_validation(password):
    if bool(re.search(control1,password))==False:
        raise ValueError("This password is not valid. You should use at least one lower letter.")
    elif bool(re.search(control2,password))==False:
        raise ValueError("This password is not valid. You should use at least one upper letter.")
    elif bool(re.search(control3,password))==False:
        raise ValueError("This password is not valid. You should use at least one digit.")
    elif bool(re.search(control4,password))==False:
        raise ValueError("This password is not valid. You should use at least one of them ($,#,@).")
    elif bool(re.search(control5,password))==False:
        raise ValueError("This password is not valid. You should use at least 6 characters and max 16 chacters.")
    else:
        return 'Password is valid.'
print(password_validation(input("")))    # aAzc1$22