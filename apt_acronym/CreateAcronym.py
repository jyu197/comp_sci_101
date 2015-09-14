'''
Created on Sep 10, 2015

@author: Jonathan Yu
'''

def acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym = acronym + word[0]
    return acronym

if __name__ == '__main__':
    pass