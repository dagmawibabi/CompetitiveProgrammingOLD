#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    if len(grades) > 1 and len(grades) < 60:
        for i in range(len(grades)):
            if grades[i] > 37:
                if grades[i] % 5 == 0:
                    grades[i] = grades[i]
                elif grades[i] % 10 <= 4:
                    next_x5 = (grades[i] - (grades[i] % 10) + 5)
                    if (next_x5 - grades[i] >= 3 ):
                        grades[i] = grades[i]
                    else:
                        grades[i] = next_x5
                else:
                    next_x5 = (grades[i] - (grades[i] % 10) + 10)
                    if (next_x5 - grades[i] >= 3 ):
                        grades[i] = grades[i]
                    else:
                        grades[i] = next_x5
                
            else:
                return grades      
    else:
        print("incorrect grade number")
                    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
