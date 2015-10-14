'''
Created on Oct 4, 2015

@author: ola
'''

def guessLetters(word):
    guess = ['_']*len(word)
    misses = 0
    
    while True:
        if guess.count('_') == 0:
            break
        print "guessing", ''.join(guess)
        letter = raw_input("guess a letter: ")
        if letter in guess:
            print "that letter was already guessed"
            continue
        if letter not in word:
            print "that's a miss"
            misses += 1
        else:
            print "you guessed a letter"
        for index in range(len(word)):
            if word[index] == letter:
                guess[index] = letter
    print misses

if __name__ == '__main__':
    guessLetters("fabulous")