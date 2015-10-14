'''
Created on Sep 11, 2015

@author: Jonathan Yu
'''

def minutesNeeded(numCakes, capacity):
    if numCakes % capacity == 0:
        return numCakes / capacity * 10
    elif numCakes % capacity > capacity/2:
        return numCakes / capacity * 10 + 10
    else:
        return numCakes / capacity * 10 + 5

if __name__ == '__main__':
    pass