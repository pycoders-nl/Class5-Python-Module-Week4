from math import gcd
import math
numbers = []
n = int(input("how many numbers?:"))
count=0
while True:
    count+=1
    if count==n+1:
        break
    try:
        number=int(input("enter numbers"))
        numbers.append(int(number))
    except ValueError:
        print("Enter a valid number")
        count-=1
print(math.gcd(*numbers))





