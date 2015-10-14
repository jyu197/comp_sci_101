'''
Created on Sep 15, 2015

@author: Jonathan Yu
'''

def modify(name):
    names = name.split()
    if len(names) == 1:
        return name
    last_name_first = names[len(names) - 1] + ", " + names[0]
    names = names[1:len(names)-1]
    for word in names:
        if len(word) == 1:
            last_name_first = last_name_first + " " + word[0]
        else:
            last_name_first = last_name_first + " " + word[0] + "."
    return last_name_first

if __name__ == '__main__':
    pass