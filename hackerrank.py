### Diagonal Difference

def difference(arr, n):
	d1 = 0
	d2 = 0

	for i in range(0, n):
		d1 += arr[i][i]
		d2 += arr[i][n - i - 1]
	return abs(d1 - d2)
n = 3
arr = [[11, 2, 4],
	  [4 , 5, 6],
	  [10, 8, -12]]
print("Diagonal Difference", difference(arr, n))

### Left Rotation

def leftrotate(arr,n,d):
	tem = []
	i = 0
	while (i < d):
		tem.append(arr[i])
		i += 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i += 1
		d += 1
	arr[:] = arr[: i] + tem
	return arr
arr = [0,7,1,9,0,7,1,9]
print("Left Rotation", leftrotate(arr, len(arr), 2))

### Counter Game

def counterGame(n):
    n = bin(n)[2:]
    n = n.split('1')
    turns = len(n)+len(n[-1])-2
    return 'Louise' if turns&1 else 'Richard'
print(counterGame(132))

### Time Delta
from datetime import datetime

time_format  = "%a %d %b %Y %H:%M:%S %z"
for i in range(int(input("Please entry comparison places: "))):
    time1 = datetime.strptime(input("Please entry this date, time and zone: "), time_format )
    time2 = datetime.strptime(input("Please entry this date, time and zone: "), time_format )
print(int(abs((time1 - time2).total_seconds())))