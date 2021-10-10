from random import randint

def rollDice():
    global number
    number = int(input('how many times? '))
    global dice
    dice=[0,0,0,0,0,0]
    for i in range(1,number):
        x =randint(1,6)
        dice[x-1]+=1
    # print(dice)
    return ret()

def ret():
    for i in range(6):
        print(f"The probability of {i+1} is : ""%.2f"%(dice[i]/number*100))

rollDice()
