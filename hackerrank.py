# 1. Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
    n=int(input(''))
    x1=[arr[i][i]for i in range(n)]
    x2=[arr[n-i-1][i]for i in range(n)]
    return abs(sum(x1)-sum(x2))

# 2. Left Rotation: https://www.hackerrank.com/challenges/array-left-rotation/problem
def rotateLeft(d, arr):
    for i in range(d):
        arr.append(arr[0])
        arr.pop(0)
    return arr

# 3. Counter game: https://www.hackerrank.com/challenges/counter-game/problem
import math
def closest_power_of_2(n):
    return 2**math.floor(math.log(n,2))

def counterGame(n):
    string=['Louise','Richard']
    counter_string=-1
    while n!=1:
        counter_string+=1 # l
        closest=closest_power_of_2(n)
        if closest==n:
            n=n/2
        else:
            n=n-closest
    return string[counter_string%2]

# 4. Time Delta: https://www.hackerrank.com/challenges/python-time-delta/problem
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    ti1=datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    ti2=datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    ti3=ti1-ti2
    return str(abs(ti3.days*86400+ti3.seconds))