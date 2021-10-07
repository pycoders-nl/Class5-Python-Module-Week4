def rollDice(repetitions_number, W_number):
    import random 
    dice = [0, 0, 0, 0, 0, 0]

    for i in range(repetitions_number):
        x = random.randrange(1, 7)
        dice[x-1]+=1 
    percentage= dice[W_number-1]/repetitions_number*100
    return percentage