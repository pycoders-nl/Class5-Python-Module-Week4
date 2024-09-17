from random import randint
def rollDice(number):
    dice=[0]*6 #[0,0,0,0,0,0]
    for i in range(number):
        dice[randint(1,6)-1]+=1 #specify the index => [randint(1,6)-1]
    dice=[round((dice[i]/number)*100,2) for i in range(len(dice))]
    return dice
