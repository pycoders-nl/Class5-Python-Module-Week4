# ## 2. Dice Percentage
# * Create an array with 6 elements named `dice`. Fill this array with the value zero. Generate a random number with a value between 1 and 6 (just like a **dice**) in a repetition 5000 times.

# * If the value is 1, increase the element 0 in the array by 1, the same applies to the values 2, 3, 4, 5 and 6. The dice[0] element indicates the number of times value 1 has occurred. Or in general: dice[x-1] indicates the number of times that x has been thrown. 
    
# * At the end of the repetition, print the contents of the array as percentages with 2 decimal places. For example; `"Percentage of throws of value 3 = 16.28%"`

from random import randint
dice=[0]*6 # create a dice list with 6 elements
for i in range(5000):#generate 5000 number between 1 and 6
    dice[randint(1,6)-1]+=1
for i in range(len(dice)):
    print('Percentage of throws of value {} = {:.2f}%'.format(i+1,(dice[i]/5000)*100))