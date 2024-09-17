import my_dice
dice=my_dice.rollDice(int(input("Enter repetition number: ")))
for i in range(len(dice)):
    print("The probability of {} is {}%".format(i+1,dice[i]))