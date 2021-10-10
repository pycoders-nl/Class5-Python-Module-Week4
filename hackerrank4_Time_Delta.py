#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    t_format = "%a %d %b %Y %H:%M:%S %z"
    zaman_1 = datetime.strptime(t1, t_format)
    zaman_2 = datetime.strptime(t2, t_format)
    sonuc = int(abs((zaman_1 - zaman_2).total_seconds()))
    #sonuc = int(abs(((datetime.strptime(t1, t_format)) - (datetime.strptime(t2, t_format))).total_seconds()))
    
    return str(sonuc)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
