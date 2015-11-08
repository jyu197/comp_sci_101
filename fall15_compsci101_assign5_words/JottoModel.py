'''
Created on Oct 6, 2015

@author: Jonathan Yu
'''
import random

allWords = []
words = []
guesses = 0

def loadWords(filename):
    '''
    load words from specified file into a global list
    '''
    global allWords
    f = open(filename)
    st = f.read()
    allWords = st.split()
    #error checking
    for w in allWords:
        if len(w) != 5:
            print "error:",w
            
def getGuess():
    '''
    return random string chosen from appropriate global variable,
    update global count of number of guesses
    '''
    global words
    global guesses
    guesses += 1
    return random.choice(words)

def guessCount():
    '''
    return number of guesses made in model
    '''
    global guesses
    return guesses

def startGame():
    '''
    initialize global variables used in playing one game
    '''
    global allWords
    global words
    global guesses
    words = allWords
    guesses = 0

def processCommon(guess, count):
    '''
    set global variable to only those words that have count letters
    in common with guess, also remove guess from global variable
    '''
    global words
    words = [w for w in words if common(guess, w) == count]
    if guess in words:
        words.remove(guess)
    return len(words)

def common(a,b):
    """
    Returns number of letters in common between given strings a and b,
    no matter where those letters occur within the strings
    """
    alist = list(a)
    blist = list(b)
    for c in alist:
        if c in blist:
            blist[blist.index(c)] = '*'
    return blist.count("*")

if __name__ == '__main__':
    pass
