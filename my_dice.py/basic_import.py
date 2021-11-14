import dice_percentage

while True : 
    print("press q for exit")
    repetition = input("repetition : ")
    if repetition == "q" or repetition == "Q":
        break
    else : 
        repetition = int(repetition)
        print(f"percentage of throws of value 1 = {dicepercentage.percentage(1,repetition):.2f} %") # we wanted only 2 decimal . in print (f"{number:.2f}") with that way.
        print(f"percentage of throws of value 2 = {dicepercentage.percentage(2,repetition):.2f} %")
        print(f"percentage of throws of value 3 = {dicepercentage.percentage(3,repetition):.2f} %")
        print(f"percentage of throws of value 4 = {dicepercentage.percentage(4,repetition):.2f} %")
        print(f"percentage of throws of value 5 = {dicepercentage.percentage(5,repetition):.2f} %")
        print(f"percentage of throws of value 6 = {dicepercentage.percentage(6,repetition):.2f} %")
