# ## 1. Password
# Write a Python program to check the validity of a password (input from users)
    
# **Rules :**
# - At least 1 letter between [a-z] and 1 letter between [A-Z]
# - At least 1 number between [0-9].
# - At least 1 character from [$#@].
# - Minimum length 6 characters.
# - Maximum length 16 characters.
# If password is not valid throw `ValueError` with a proper error message for each rule. If the password is valid print a success message. Use some from  `raise`, `except`, `assert`, `else` and `finally` keywords.
#First way
import re
def password_validation(password):
    if bool(re.findall("^.*(?=.{6,16}).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least 6 characters and max 16 chacters.")
    elif bool(re.findall("^.*(?=.*[A-Z]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one upper letter.")
    elif bool(re.findall("^.*(?=.*[0-9]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one digit.")
    elif bool(re.findall("^.*(?=.*[$#@]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one of them ($,#,@).")
    elif bool(re.findall("^.*(?=.*[a-z]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one lower letter.")
    else:
        return 'Password is valid.'
print(password_validation(input("")))    # aAzc1$22 

#second way
import re
def password_validation(password):
    if bool(re.findall("^.*(?=.{6,16}).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least 6 characters and max 16 chacters.")
    elif bool(re.findall("^.*(?=.*[A-Z]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one upper letter.")
    elif bool(re.findall("^.*(?=.*[0-9]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one digit.")
    elif bool(re.findall("^.*(?=.*[$#@]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one of them ($,#,@).")
    elif bool(re.findall("^.*(?=.*[a-z]).*$",password))==False:
        raise ValueError("This password is not valid. You should use at least one lower letter.")
    else:
        return 'Password is valid.'
try:
    print(password_validation(input("")))    # aAzc1$22 
except ValueError as e:
    print(ValueError,e)