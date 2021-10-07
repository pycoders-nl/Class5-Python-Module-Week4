import re
password=input("Şifre giriniz:")
def Password(password):
	x=True
	while x:
		if len(password)<6 or len(password)>16 : 
			raise ValueError("Password has to between 6-16 characters.")
		elif not re.search("[a-z]",password):
			raise ValueError ("Password must have at least 1 letter between [a-z]")
		elif not re.search("[A-Z]",password):
			raise ValueError("Password must have at least 1 letter between [A-Z]")
		elif not re.search("[0-9]",password):
			raise ValueError("Password must have at least 1 number between [0-9]")
		elif not re.search("[$#@]",password):
			raise ValueError("Password must have at least 1 charachter between [$#@]")
		else:
			print("Congratulations,Valid Password")
			x=False
			break
		
try:
	Password(password)

except ValueError as V : 
        print(V)

finally:
	print("Don't give up")

