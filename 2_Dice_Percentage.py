from random import randint
dice=[0,0,0,0,0,0]
for i in range(1,5001):
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
print(dice)
for i in range(6):
    print('Percentage of throws of value {} =: {:.2%}'.format((i+1),(dice[i]/5000)))
