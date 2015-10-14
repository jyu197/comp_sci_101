'''
Created on Oct 13, 2015

@author: Jonathan Yu
'''

def numberUnique(zoos):
    numUnique = 0
    for zoo in zoos:
        otherAnimals = []
        for otherZoo in zoos:
            if otherZoo != zoo:
                otherAnimals.extend(otherZoo.split(" "))
        if not (set(zoo.split(" ")) <= set(otherAnimals)):
            numUnique += 1
    return numUnique

if __name__ == '__main__':
    pass