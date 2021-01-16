# Source: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    count=0
    i=0
    while i<=len(c)-1:
        
        if i+2<len(c):
            if c[i+2]==0:
                count+=1
                i+=2
            else:
                count+=1
                i+=1
        else:
            count+=1
            i+=1
    return(count-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
