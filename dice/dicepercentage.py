"""Create an array with 6 elements named `dice`. Fill this array with the value zero. 
Generate a random number with a value between 1 and 6 (just like a **dice**) in a repetition 5000 times.

If the value is 1, increase the element 0 in the array by 1, the same applies to the values 2, 3, 4, 5 and 6.
 The dice[0] element indicates the number of times value 1 has occurred. Or in general: 
 dice[x-1] indicates the number of times that x has been thrown. 
    
At the end of the repetition, print the contents of the array as percentages with 2 decimal places.
 For example; `"Percentage of throws of value 3 = 16.28%"""

import random
def rolldice(likelihood):
    """
    This functions takes 1 argument which you want to likelihood of dice.
    it returns 6 digit in list , after count whole surface of dice.
    """
    dice = [0,0,0,0,0,0]
    result = [random.randrange(1,7) for i in range(likelihood)] #writed whole possibility in a list.
    for i in range(1,7): #changed index that how many number it counted.
        dice[i-1] = result.count(i) 
    return dice
def percentage(part,likelihood):
    """
    This function works with rolldice() function .it takes 2 argument and first one
    which side you want to look and second one is likelihood ."""
    return 100 * float(rolldice(likelihood)[part-1])/float(likelihood) #called first dicegenerator function after it looked index before convert float.
if __name__ == "__main__" : 

    print(f"percentage of throws of value 1 = {percentage(1,5000):.2f} %") # we wanted only 2 decimal . in print (f"{number:.2f}") with that way.
    print(f"percentage of throws of value 2 = {percentage(2,5000):.2f} %")
    print(f"percentage of throws of value 3 = {percentage(3,5000):.2f} %")
    print(f"percentage of throws of value 4 = {percentage(4,5000):.2f} %")
    print(f"percentage of throws of value 5 = {percentage(5,5000):.2f} %")
    print(f"percentage of throws of value 6 = {percentage(6,5000):.2f} %")
