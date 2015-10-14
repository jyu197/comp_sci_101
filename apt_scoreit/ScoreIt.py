'''
Created on Sep 20, 2015

@author: Jonathan Yu
'''

def maxPoints(toss):
    best = 0
    for roll in [1,2,3,4,5,6]:
        if roll * toss.count(roll) > best:
            best = roll * toss.count(roll)
    return best

if __name__ == '__main__':
    pass