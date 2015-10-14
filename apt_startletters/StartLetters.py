'''
Created on Oct 13, 2015

@author: Jonathan Yu
'''

def howManyLetters(phrase):
    words = phrase.split()
    letters = []
    for word in words:
        letters.append(word[0].lower())
    return len(set(letters))

if __name__ == '__main__':
    pass