# Source : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys
from string import ascii_lowercase

def designerPdfViewer(h, word):
    letters = {letter: x for x, letter in enumerate(ascii_lowercase)}
    length = max(h[letters[i]] for i in word)
    print(length)
    return len(word)*length
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
