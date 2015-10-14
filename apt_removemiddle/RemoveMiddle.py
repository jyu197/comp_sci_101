'''
Created on Sep 15, 2015

@author: Jonathan Yu
'''

def shorten(name):
    names = name.split()
    if len(names) > 1:
        return names[0] + " " + names[len(names)-1]
    else:
        return names[0]

if __name__ == '__main__':
    pass