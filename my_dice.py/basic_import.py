import dice_percentage

while True : 
    print("Please press Q for exit")
    repetition = input("repetition : ")
    if repetition == "Q" or repetition == "p":
        break
    else : 
        repetition = int(repetition)
        print(f"percentage of throws of value 1 = {dice_percentage.percentage(1,repetition):.2f} %")
        print(f"percentage of throws of value 2 = {dice_percentage.percentage(2,repetition):.2f} %")
        print(f"percentage of throws of value 3 = {dice_percentage.percentage(3,repetition):.2f} %")
        print(f"percentage of throws of value 4 = {dice_percentage.percentage(4,repetition):.2f} %")
        print(f"percentage of throws of value 5 = {dice_percentage.percentage(5,repetition):.2f} %")
        print(f"percentage of throws of value 6 = {dice_percentage.percentage(6,repetition):.2f} %")
