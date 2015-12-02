'''
Created on Dec 2, 2015

@author: Jonathan
'''

from operator import itemgetter

def sizings(words):
    words = sorted(list(set(words)))
    words = [(word, len(word)) for word in words]
    return [w[0] for w in sorted(words, key = itemgetter(1))]

if __name__ == '__main__':
    pass