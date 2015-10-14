'''
Created on Oct 4, 2015

@author: ola
'''
from pywin.scintilla.formatter import wordstarts
def readWords():
    f = open("lowerwords.txt")
    return f.read().split()

def countLen(words, length):
    '''
    return the number of strings in words whose length is 
    the value of parameter length. So if length is 3, this is
    the number of 3-letter strings in words
    '''
    return sum([1 for word in words if len(word) == length])

def stars(num):
    '''
    returns a string containing one asterisk for each time
    num is fully divisible by 150, e.g., num/150 asterisks. 
    If this is zero, return a string with a single asterisk
    '''
    if num / 150 == 0:
        return "*"
    return "*" * (num / 150)

def wordLengths(words):
    total = 0
    for length in range(1,33):
        val = countLen(words,length)
        total += val
        if val > 0:
            print length, "\t", val, "\t", stars(val)
    return total

if __name__ == '__main__':
    words = readWords()
    print "read",len(words),"words"
    total = wordLengths(words)
    print "value returned",total
