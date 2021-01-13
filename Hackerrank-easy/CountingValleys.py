# Source: https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    c1=0
    a=[]
    v=0
    for i in path:
        if i=='U':
            c1+=1                
        elif i=='D':
            c1+=-1
        if i=='U'and c1==0:
            v+=1
    return(v)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
