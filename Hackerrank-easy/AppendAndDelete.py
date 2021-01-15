# Source: https://www.hackerrank.com/challenges/append-and-delete/problem

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    index = -1
    if s==t:
        if k%2==0 or k>=(2*len(s)):
            return "Yes"
        else:
            return "No"
    if len(s) < len(t):
        n = len(s)
    else:
        n = len(t)
    breaker = False
    for i in range(n):
        if s[i] != t[i]:
            index = i
            breaker = True
            break
    if breaker == False:
        index = n-1 
    n1 = len(s) - index 
    n2 = len(t) - index 
    print(n1, n2, index)
    num = n1 + n2
    num_even = True
    if num%2 == 0:
        num_even = True
    else:
        num_even = False
    print(num_even, k>=num)
    if index == 0 and k>=num:
        return "Yes"
    elif num_even and (k >= num and k%2==0):
        return "Yes"
    elif num_even == False and k >=num and k%2 == 1:
        return "Yes"
    else:
        return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()