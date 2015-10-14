'''
Created on Sep 22, 2015

@author: Jonathan Yu
'''

def satisfies(stuff):
    num = 0
    for word in stuff:
        if word[len(word) - 1] == "a":
            num = num + 1
    return num

if __name__ == '__main__':
    pass