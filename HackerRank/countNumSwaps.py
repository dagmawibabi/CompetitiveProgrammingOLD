#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swapCount = 0;
    n = len(a);
    for i in range(0, n):
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                b = a[j]
                a[j] = a[j + 1];
                a[j + 1] = b;
                swapCount += 1;

    print("Array is sorted in " + str(swapCount) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
