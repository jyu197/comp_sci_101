'''
Created on Nov 17, 2015

@author: Jonathan
'''

def most(words):
    mostWord = ""
    mostCount = 0
    for word in reversed(sorted(list(set(words)))):
        if words.count(word) > mostCount:
            mostWord = word
            mostCount = words.count(word)
    return mostWord

if __name__ == '__main__':
    pass