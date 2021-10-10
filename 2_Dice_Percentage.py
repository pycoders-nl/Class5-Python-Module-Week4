from random import randint
dice=[0,0,0,0,0,0]
for i in range(1,5001):
    x =randint(1,6)
    dice[x-1]+=1
print(dice)
for i in range(6):
    print('Percentage of throws of value {} =: {:.2%}'.format((i+1),(dice[i]/5000)))