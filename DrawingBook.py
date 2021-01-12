# Source: https://www.hackerrank.com/challenges/drawing-book/problem

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    f=0
    if p%2==0:
        f=p/2
        
        
    else:
        f=(p-1)/2
        
    
    pages = n//2
    b = pages-f
    return int(min(f,b))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
