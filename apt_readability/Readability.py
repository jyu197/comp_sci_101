'''
Created on Sep 22, 2015

@author: Jonathan Yu
'''

def asl(measurable):
    words = measurable.split(" ")
    punctuation = [".", "?", "!"]
    numWords = 0.0
    numSentences = 0
    for word in words:
        numWords = numWords + 1
        for char in punctuation:
            if word.count(char) != 0:
                numSentences = numSentences + 1
                break;
    if numSentences == 0:
        return 0.0
    return numWords / numSentences

if __name__ == '__main__':
    pass