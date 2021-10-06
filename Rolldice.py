#dice percentage
import random

def percent(number):
    dice=[0,0,0,0,0,0]# I created an array with 6 elements named dice and I filled this array with the value zero.
    n=5000
    for i in range(n):
        number=random.randint(1,6)# It will generate a random number with a value between 1 and 6 in a repetition 5000 times.
        if number==1:#If the value is 1, increase the element 0 in the array by 1
            dice[0]+=1
        elif number==2:#It is the same for each numbers
            dice[1]+=1
        elif number==3:
            dice[2]+=1
        elif number==4:
            dice[3]+=1
        elif number==5:
            dice[4]+=1
        else:
            dice[5]+=1
    percentage=dice[number-1]/n*100 #At the end of the repetition i calculated percentages with 2 decimal places.
    return percentage # I wanted to return percentage
    

print("Percentage of throws of value","4","=",percent(4),"%") #I wrote it to the screen
