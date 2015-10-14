'''
Created on Oct 13, 2015

@author: Jonathan Yu
'''

def whichOrder(available, orders):
    for order in orders:
        if set(order.split(" ")) <= set(available):
            return orders.index(order)
    return -1

if __name__ == '__main__':
    pass