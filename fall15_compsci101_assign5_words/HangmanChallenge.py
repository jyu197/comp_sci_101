'''
Created on Oct 20, 2015

@author: Jonathan Yu
'''
import random

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
    blanks = []
    for ch in secret:
        '''
        Only replace alphabetic characters with spaces,
        so the user doens't have to guess punctuation,
        spaces, or numbers
        '''
        if ch.isalpha():
            blanks.append("_")
        else:
            blanks.append(ch)
    return blanks

def doGame(word):
    guess = makeSecretList(word)
    missesAllowed = 8
    misses = 0
    lettersNotGuessed = "abcdefghijklmnopqrstuvwxyz"
    
    while True:
        if guess.count('_') == 0:
            break
        print ""
        print "number of misses left: " + str(missesAllowed - misses)
        print "letters not yet guessed: " + lettersNotGuessed
        print "secret so far:",display(guess)
        letter = raw_input("guess a letter: ").lower()
        if letter not in lettersNotGuessed:
            #if letter has already been guessed, does not count as a miss
            continue
        lettersNotGuessed = lettersNotGuessed.replace(letter, " ")
        success = False
        for index in range(len(word)):
            if word[index].lower() == letter:
                guess[index] = word[index]
                success = True
        if not success:
            misses += 1
        if misses == missesAllowed:
            break
            
    if guess.count("_") == 0:
        print "word is guessed!",word
    else:
        print "you lost! word is",word
 
def play(allwords):
    print "Guess the song!"
    word = random.choice(allwords)
    doGame(word)

if __name__ == '__main__':
    allwords = loadWords("songs.txt")
    play(allwords)