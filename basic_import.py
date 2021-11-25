import dice
ddice=dice.rollDice(int(input("Enter repetition number: ")))
for i in range(len(ddice)):
    print("The probability of {} is {}%".format(i+1,ddice[i]))
    