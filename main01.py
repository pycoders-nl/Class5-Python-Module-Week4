
#Create a new module called `main.py`. 
# Gets an input from the user using `"Enter repetition number: "`. 
# Then call rollDice method with this user input. 
# Lastly, print each probability. E.g. `"The probability of 0 is 16.20"`

import my_dice 
repetitions_number = int(input("How many times do you want to roll:")) 
W_number = int(input("which number's percentage:"))  
print("The probability ",W_number, my_dice.rollDice(repetitions_number, W_number), "%") 