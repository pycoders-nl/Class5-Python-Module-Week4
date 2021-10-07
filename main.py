import my_dice # calling  the new module my_dice
repetition = int(input("entre repetition number:")) # getting an input from the user using "Enter repetition number:
number = int(input("which number's percentage:"))  # getting an input from the user for using "which number's percentage:"
print("The probability of",number,"is", my_dice.rollDice(repetition, number), "%")