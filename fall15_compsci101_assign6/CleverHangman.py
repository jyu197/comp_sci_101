'''
Created on Nov 20, 2015

@author: Jonathan
'''
import random

testingMode = False

def loadWords(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    allwords = []
    f = open(filename)
    for line in f:
        line = line.strip()
        allwords.append(line)
    f.close()
    return allwords

def getWords(allwords,wordlength):
    """
    returns a list of words having a specified length from
    allwords
    """
    wlist = [w for w in allwords if len(w) == wordlength]
    return wlist

def display(guess):
    '''
    create a string from list guess to print/show user
    '''
    return ' '.join(guess)

def makeSecretList(secret):
    '''
    Create the list that's modificable to track letters 
    guessed by user
    '''
    return ['_']*len(secret)

def categorize(words, guess, letter):
    '''
    determine the template, with the most choices in parameter
    words, that is consistent with the current template,
    parameter guess, and the guessed character, parameter letter
    
    return the template and the words that match the template
    ''' 
    cleverWords = {}
    for w in words:
        category = list(guess)
        for i in range(len(w)):
            if w[i] == letter:
                category[i] = w[i]
        category = "".join(category)
        if category not in cleverWords:
            cleverWords[category] = [w]
        else:
            cleverWords[category].append(w)
    if testingMode:
        print "Dictionary of Categories and # words:"
        for category in cleverWords:
            print category + " " + str(len(cleverWords[category]))
        print "-------"
    cleverWordLengths = cleverWords.copy()
    for category in cleverWordLengths:
        '''
        create a copy of the category dictionary where the values
        are the lengths of the lists of matching words, not the lists
        themselves (easier to find template with maximum number of 
        matching words)
        '''
        cleverWordLengths[category] = len(cleverWordLengths[category])
    guess = max(cleverWordLengths, key = cleverWordLengths.get)
    return guess, cleverWords[guess]

def doGame(words):
    '''
    play the individual rounds of Hangman
    '''
    missesAllowed = int(raw_input("how many misses are allowed? "))
    misses = []
    word = random.choice(words)
    guess = makeSecretList(word)
    
    while True:
        if guess.count('_') == 0:
            break
        print
        if testingMode:
            print "(secret word: " + word + ")"
            print "# words possible:", len(words) 
        print "Progress:", display(guess)
        print "number of misses left:", missesAllowed - len(misses)
        print "letters missed:", " ".join(misses)
        letter = raw_input("guess a letter: ").lower()
        if (letter in misses) | (letter in guess):
            #if letter has already been guessed, guess again
            continue
        guess, words = categorize(words, guess, letter)
        word = random.choice(words)
        if letter in guess:
            print "you guessed a letter correctly!"
        else:
            print letter + " not in secret word"
            misses.append(letter)
        if len(misses) == missesAllowed:
            break
    
    if guess.count("_") == 0:
        print "word is guessed!", word
    else:
        print "You are hung! word was", word
 
def play(allwords):
    '''
    start a game of Hangman
    '''
    global testingMode
    
    print "Welcome to the Hangman game."
    print "Do you want to play the game (g) or show the testing mode (t)?"
    mode = raw_input("Type g or t: ")
    if mode == "t":
        testingMode = True
    else:
        testingMode = False
    wlen = int(raw_input("how many letters in word you'll guess (3 or greater)? "))
    words = getWords(allwords,wlen)    
    doGame(words)

if __name__ == '__main__':
    allwords = loadWords("lowerwords.txt")
    play(allwords)