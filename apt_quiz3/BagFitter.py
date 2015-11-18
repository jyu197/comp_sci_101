'''
Created on Nov 17, 2015

@author: Jonathan
'''

def bags(strength, food):
    numBags = 0
    for type in set(food):
        if food.count(type) % strength == 0:
            numBags += food.count(type) / strength
        else:
            numBags += food.count(type) / strength + 1
    return numBags

if __name__ == '__main__':
    pass