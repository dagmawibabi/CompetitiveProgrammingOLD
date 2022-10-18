#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    index = len(arr) - 2;
    item = arr[-1];
    itemIndex = len(arr) - 1;
    while index >= 0:
        if arr[index] < item:
            # arr[index] = item;
            arr[index + 1] = item;
        else:
            arr[index + 1] = arr[index];
        index -= 1;
        print(' '.join(str(i) for i in arr));


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
