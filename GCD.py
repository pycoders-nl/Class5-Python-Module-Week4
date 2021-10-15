
from functools import reduce
def inputs():
	try:
		global x,y
		x=int(input("enter first number:"))
		y=int(input("enter second number:"))
	except ValueError:
		print("Invalid. Please write a valid number")

def Gcd():
	return gcd(x,y)

if __name__ == '__main__':
	inputs()
print(Gcd())
