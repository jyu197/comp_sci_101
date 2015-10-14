'''
Created on Sep 21, 2015

@author: Jonathan Yu
'''

def coins(pence):
    return [pence / 240, (pence - pence / 240 * 240) / 12, pence - (pence / 240 * 240 + (pence - pence / 240 * 240) / 12 * 12)]

if __name__ == '__main__':
    pass