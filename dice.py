from random import randint
def rollDice(number):
    dice=[0,0,0,0,0,0]
    for i in range(1,5001):   
        dice[randint(1,6)-1]+=1
    for i in range(6):
        print('Percentage of throws of value {} =: {:.2%}'.format((i+1),(dice[i]/5000))) 