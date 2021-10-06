# a program which can calculate the greatest common divisor (GCD) of my inputs.
import math
def gcd():
    count=int(input("How many numbers do you want to enter: "))#I asked the number of the enters
    numbers=[] #I opened a new list with the name numbers.
    
    a=0
    while a<count:#it is going to turn until this formula
        try: #I used try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
            new=int(input("please enter new number"))
        except Exception:
            print("Please do not enter Nan or non numerical numbers.")
        else:
            numbers.append(new)
            a+=1

    gcdr=math.gcd(numbers[0],numbers[1])#i tried to find gcd in numbers list for first two elements with gcd module. its name is gcdr
    for i in range(2,len(numbers)):#then I started from third element in numbers list and i turned it with each elements.
        gcdreal=int(math.gcd(gcdr,numbers[i]))#every turn it is going to be change.
    
    return gcdreal #then i want to return gcdreal for the gcd numbers in numbers list

print("gcd is: ",gcd())