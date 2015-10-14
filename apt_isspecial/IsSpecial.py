'''
Created on Sep 22, 2015

@author: Jonathan Yu
'''

def lovely(ingrediants, inedible):
    ingrediants = ingrediants.split(" ")
    inedibles = inedible.split(" ")
    edible = 0
    for ingrediant in ingrediants:
        if ingrediant not in inedibles:
            edible = edible + 1
    return edible

if __name__ == '__main__':
    pass