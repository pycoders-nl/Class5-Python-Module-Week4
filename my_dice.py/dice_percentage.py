### Create an array with 6 elements named dice. Fill this array with the value zero.
### Generate a random number with a value between 1 and 6 (just like a dice) in a repetition 5000 times.



import numpy as np                                      # I used some 'Modelus'

def dice_perc(x):
    np.random.seed(1907)
    dice = np.array([1,2,3,4,5,6])
    dice_1 = []
    for i in range(int(5000)):
        turn = np.random.choice(dice)
        dice_1.append(int(turn))
    d1c = dice_1.count(1)
    d2c = dice_1.count(2)
    d3c = dice_1.count(3)
    d4c = dice_1.count(4)
    d5c = dice_1.count(5)
    d6c = dice_1.count(6)
    per_1 = d1c/5000
    per_2 = d2c/5000
    per_3 = d3c/5000
    per_4 = d4c/5000
    per_5 = d5c/5000
    per_6 = d6c/5000

    percentage = ("Percentage of throws of value 1: {:.2%}\nPercentage of throws of value 2: {:.2%}\n"
                "Percentage of throws of value 3: {:.2%}\nPercentage of throws of value 4: {:.2%}\n"
                "Percentage of throws of value 5: {:.2%}\nPercentage of throws of value 6: {:.2%}"
                .format(per_1,per_2,per_3,per_4,per_5,per_6))
    return percentage
print(dice_perc(5000))