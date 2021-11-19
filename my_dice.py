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
     dice=[0,0,0,0,0,0]
     per=[0,0,0,0,0,0]
     for i in range(n):
         hand = random.randint(1,6)
         for x in range (1,7):
            if hand==x:
              dice[x-1]+=1
              per[x-1]=("{:.2f}".format((dice[x-1]*100/n)))
     Per=[]
     for i in range(6):
         current=(dice[i]*100/n)#generates percentages for (1,6) 
         Per.append(current)    
  
     # per=[("{:.2f}".format((dice[0]*100/n))),("{:.2f}".format((dice[1]*100/n))),("{:.2f}".format((dice[2]*100/n)))
     #      ,("{:.2f}".format((dice[3]*100/n))),("{:.2f}".format((dice[4]*100/n))),("{:.2f}".format((dice[5]*100/n)))]
     return per
