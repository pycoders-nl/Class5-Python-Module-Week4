import math
from functools import reduce
try:
    n= int(input())
except ValueError as v:
    print(v)
try:
    lijst= map(int,input(f'{n} tane sayi boslukla ayrarak giriniz :').split())
except ValueError as v:
    print(v)
lijst = list(lijst)
print(lijst)
gcd1=0
for x in range(1,n):
    if x ==1:
        gcd1= math.gcd(lijst[0],lijst[1])
    else:
        gcd1=math.gcd(gcd1,lijst[x])
print(gcd1)
