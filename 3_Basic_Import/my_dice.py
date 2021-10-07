from random import randint

def rollDice():
    global number
    number = int(input('how many times? '))
    global dice
    dice=[0,0,0,0,0,0]
    for i in range(1,number):
        zar_atma =randint(1,6)
        if zar_atma ==1:
            dice[0]+=1
        elif zar_atma ==2:
            dice[1]+=1
        elif zar_atma ==3:
            dice[2]+=1
        elif zar_atma ==4:
            dice[3]+=1
        elif zar_atma ==5:
            dice[4]+=1
        elif zar_atma ==6:
            dice[5]+=1
    # print(dice)
    return ret()

def ret():
    for i in range(6):
        print(f"The probability of {i+1} is : ""%.2f"%(dice[i]/number*100))

rollDice()
