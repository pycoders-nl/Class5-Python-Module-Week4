#Python program to check the validity of a password (input from users)
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12): #I asked all of the requirements
        raise ValueError("The length of the password is not valid")#If there is a not valid enter,it will raise a error in each situation.
        break
    elif not re.search("[a-z]",p):
        raise ValueError("There is no lower case in your password")
        break
    elif not re.search("[0-9]",p):
        raise ValueError("There is no number in your password")
        break
    elif not re.search("[A-Z]",p):
        raise ValueError("There is not a upper case in your password")
        break
    elif not re.search("[$#@]",p):
        raise ValueError("There is not a special character in your password")
        break
   
    else:
        print("Valid Password")#If all of the possibilities are true, it will write valid password to the screen.
        x=False
        break