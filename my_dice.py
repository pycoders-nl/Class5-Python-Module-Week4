from random import randint
def rollDice(number):
    dice=[0]*6 # create a dice list with 6 elements
    for i in range(number):#generate 5000 number between 1 and 6
        dice[randint(1,6)-1]+=1
    dice=[round((dice[i]/number)*100,2) for i in range(len(dice))]
    return dice

rollDice(340)