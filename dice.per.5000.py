"""Create an array with 6 elements named dice. Fill this array with the value zero. 
Generate a random number with a value between 1 and 6 (just like a dice) in a repetition 5000 times.

If the value is 1, increase the element 0 in the array by 1, the same applies to the values 2, 3, 4, 5 and 6. 
The dice[0] element indicates the number of times value 1 has occurred. 
Or in general: dice[x-1] indicates the number of times that x has been thrown.
At the end of the repetition, print the contents of the array as percentages with 2 decimal places. 
For example; "Percentage of throws of value 3 = 16.28%"""

import random
dice=[0,0,0,0,0,0] # dices in order, [1,2,3,4,5,6] .we will only add number of rounds
for i in range(5000):
  lucky_n = random.randint(1,6) #this generates dice for  current round
  for n in range (1,7):
    if lucky_n==n:       #current dice will be added in list of dice(only +1 per round)
      dice[n-1]+=1       
Per=[]
for i in range(6):
  current=(dice[i]/50) #generates percentages for (1,6) 
  Per.append(current)  #and add list(Per)
for i in range(6):
    print("Percentage of throws of Value  {} :".format(i+1),str(Per[i])+" %")

