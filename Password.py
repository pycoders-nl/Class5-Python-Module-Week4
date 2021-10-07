import re
password= input("Input your password: ")
val = True
while True:  
    if (len(password)<6 or len(password)>12): #this is password rule
        raise ValueError("Not a Valid Password") # if there is an error,it will show error message
        break
    elif not re.search("[a-z]",password):  #this is password rule
        raise ValueError("Not a Valid Password")
        break
    elif not re.search("[0-9]",password):  #this is password rule
        raise ValueError("Not a Valid Password")
        break
    elif not re.search("[A-Z]",password):  #this is password rule
        raise ValueError("Not a Valid Password")
        break
    elif not re.search("[$#@]",password):  #this is password rule 
        raise ValueError("Not a Valid Password")
        break
    else:
        print("Valid Password")
        val = False
        break