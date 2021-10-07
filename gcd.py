from math import gcd
from functools import reduce
def inputs():
	try:
		global x,y
		x=int(input("please,enter your first number:"))
		y=int(input("please enter your second number:"))
	except ValueError:
		print("Please enter your number")

def Gcd():
	return gcd(x,y)

if __name__ == '__main__':
	inputs()


print(Gcd())

