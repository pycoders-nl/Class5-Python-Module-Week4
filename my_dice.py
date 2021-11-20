"""Create a Python module called my_dice.py and export the code 
you wrote in question 2 into a function called rollDice(number).

Changes:

Instead of repetition of 5000 times, makes a repetition of times of given number variable.
Instead of printing, return the array of percentages.
Then create a new module called main.py. Gets an input from the user using "Enter repetition number: ".
 Then call rollDice method with this user input. Lastly, print each probability. E.g. 
 "The probability of 0 is 16.20"""

import random
def rollDice(n):
     dice=[0,0,0,0,0,0]          # dices in order, [1,2,3,4,5,6] .we will only add number of rounds
     Per=[]                      #list of percentages
     for i in range(n):
         hand = random.randint(1,6)
         for x in range (1,7):
            if hand==x:           #current dice will be added in list of dice(only +1 per round)
              dice[x-1]+=1 
     for i in range(6):
         current=(dice[i]*100/n)  #generates percentages for (1,6) in list(dice)
         Per.append(current)      #and add list(Per)
  
     return Per
