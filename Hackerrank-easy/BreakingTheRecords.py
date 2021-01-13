# Source: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxim = scores[0]
    minim = scores[0]
    max_count, min_count = 0, 0
    for i in scores:
        if i > maxim:
            max_count += 1
            maxim = i
        if i < minim:
            min_count += 1
            minim = i
    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
