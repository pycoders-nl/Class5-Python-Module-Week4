import re
def password_validity():
    password = input("enter a valid password")

    charRegex = re.compile(r'(\w{6,16})') 
    lowerRegex = re.compile(r'[a-z]+') 
    upperRegex = re.compile(r'[A-Z]+')
    digitRegex = re.compile(r'[0-9]+')
    chaRegex = re.compile(r'[#@$]+')

    if charRegex.findall(password)== []:
        raise ValueError('The password must be between 6 and 16 characters.')
    elif lowerRegex.findall(password)==[]:
        raise ValueError('There should be lowercase letter.')
    elif upperRegex.findall(password)==[]:
        raise ValueError('There should be uppercase letter.')
    elif digitRegex.findall(password)==[]:
        raise ValueError('There should be at least one digit.')
    elif chaRegex.findall(password)==[]:
        raise ValueError('There should be at least one of the shown special symbols.')
    else:
        print('Valid password')
password_validity()    