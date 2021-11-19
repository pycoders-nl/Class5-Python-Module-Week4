"""Create a Python module called my_dice.py and export the code
 you wrote in question 2 into a function called rollDice(number).

Changes:

Instead of repetition of 5000 times, makes a repetition of times of given number variable.
Instead of printing, return the array of percentages.
Then create a new module called main.py. Gets an input from the user using "Enter repetition number: ". 
Then call rollDice method with this user input. Lastly, print each probability. E.g. "The probability of 0 is 16.20"""

import my_dice

def dice_p(t):
  percentages=(my_dice.rollDice(t))
  
  for i in range(6):
    print("The probability of {} is {} %".format((i+1),percentages[i]))
dice_p(t=int(input("Enter repitition number :")))
