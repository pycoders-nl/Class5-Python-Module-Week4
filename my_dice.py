def rollDice(repetition, number):
    import random 
    dice = [0, 0, 0, 0, 0, 0]

    for i in range(repetition):
        j = random.randrange(1, 7)
        dice[j-1]+=1 # counting repetitions
    percentage= dice[number-1]/repetition*100 # finding the percentage of repetition
    return percentage

