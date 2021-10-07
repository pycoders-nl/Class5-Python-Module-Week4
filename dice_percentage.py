import array as arr
import random
dice = arr.array('i',[0,0,0,0,0,0])
count=0
while True:
    x= random.randint(1,6)
    count+=1
    if count== 5001:
        break
    elif x==1:
        dice[0]+=1
    elif x==2:
        dice[1]+=1
    elif x==3:
        dice[2]+=1
    elif x==4:
        dice[3]+=1
    elif x==5:
        dice[4]+=1
    elif x==6:
        dice[5]+=1
sum=dice[0]+dice[1]+dice[2]+dice[3]+dice[4]+dice[5]
print("Percentage of throws of value 0:",(dice[0]/sum)*100)
print("Percentage of throws of value 1:",(dice[1]/sum)*100)
print('Percentage of throws of value 2:',(dice[2]/sum)*100)
print("Percentage of throws of value 3:",(dice[3]/sum)*100)
print("Percentage of throws of value 4:",(dice[4]/sum)*100)
print("Percentage of throws of value 5:",(dice[5]/sum)*100)