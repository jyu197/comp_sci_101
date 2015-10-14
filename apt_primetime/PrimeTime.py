'''
Created on Sep 24, 2015

@author: Jonathan Yu
'''

import math

def pcount(low, high):
    num = 0
    for k in range(low, high + 1):
        isPrime = True
        if k < 2:
            continue
        if k == 2:
            num += 1
            continue
        for l in range(2, int(math.sqrt(k)) + 1):
            if k % l == 0:
                isPrime = False
                break
        if isPrime == True:
            num += 1
    return num

if __name__ == '__main__':
    print pcount(1, 2)
