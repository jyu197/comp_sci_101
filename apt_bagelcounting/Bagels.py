'''
Created on Sep 21, 2015

@author: Jonathan Yu
'''

def bagelCount(orders):
    bagels = 0
    for order in orders:
        bagels = bagels + order + order/12
    return bagels

if __name__ == '__main__':
    pass