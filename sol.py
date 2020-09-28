#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    x=[a+a,b+a,b+b]
    print(x)
    y=[]
    z=0
    for j in range (3,n):
        if(j%2!=0):
            for i in (x):
                y.append(i+a)
                y.append(i+b)
            y=list(set(y))
            x=[]
        else:
            for i in y:
                x.append(i+a)
                x.append(i+b)
            x=list(set(x))
            y=[]
    if(len(y)==0):
        return (sorted(x))
    else:
        return (sorted(y))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
