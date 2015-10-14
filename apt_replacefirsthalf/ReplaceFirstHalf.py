'''
Created on Sep 22, 2015

@author: Jonathan Yu
'''

def replace(phrase, newword):
    words = phrase.split(" ")
    replaced = ""
    for word in words:
        replaced = replaced + newword + word[len(word) / 2:] + " "
    return replaced.strip()    

if __name__ == '__main__':
    pass