'''
Created on Dec 2, 2015

@author: Jonathan
'''

def arrange(letter, words):
    return sorted(list(set([word for word in words if letter == word[len(word) - 1]])))

if __name__ == '__main__':
    pass