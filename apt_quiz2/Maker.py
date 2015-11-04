'''
Created on Nov 3, 2015

@author: Jonathan
'''

def canMake(message, letterlist):
    messageLetters = "".join(message).lower()
    letterlistLetters = "".join(letterlist).lower()
    if set(messageLetters) <= set(letterlistLetters):
        return "yes"
    else:
        return "no"

if __name__ == '__main__':
    pass