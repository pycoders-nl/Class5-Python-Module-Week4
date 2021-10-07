import random
dice = [0, 0, 0, 0, 0, 0]
y= int(input("which number's percentage:"))
for i in range(5000):
    x = random.randrange(1, 7)
    dice[x-1]+=1 # counting numbers
percentage= dice[y-1]/5000*100 # finding the percentage of number
print("Percentage of throws of value ", y, "=", percentage, "%" )

