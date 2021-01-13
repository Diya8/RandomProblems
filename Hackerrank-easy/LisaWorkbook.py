# Source: https://www.hackerrank.com/challenges/lisa-workbook/problem

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page_tracker = 0
    count = 0
    for i in range(n):
        temp = page_tracker
        page_tracker += arr[i]//k
        if arr[i]%k != 0:
            page_tracker += 1
        for j in range(temp, page_tracker+1):
            new_page = temp
            # check jth ques number
            new_page += j//k
            if j%k != 0:
                new_page += 1
            if j == new_page and j<=arr[i]:
                count += 1
                print("in page", j)
        
    return count-1
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
