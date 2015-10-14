'''
Created on Oct 9, 2015

@author: Jonathan Yu
'''

def count(a, b):
    count = 0
    for letter in set(a):
        count += min(a.count(letter), b.count(letter)) - 0
    return count

if __name__ == '__main__':
    pass
