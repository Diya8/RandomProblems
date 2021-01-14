# Source: https://www.hackerrank.com/challenges/permutation-equation/problem

import math
import os
import random
import re
import sys

def permutationEquation(p):
    d = {}
    li = []
    for i in range(n):
        d[p[i]] = i+1
    for i in range(n):
        li.append(d[d[i+1]])
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
