'''
Created on Sep 15, 2015

@author: Jonathan Yu
'''

def repeat(word,number):
    vowels = ["a", "e", "i", "o", "u"]
    a = word.lower()
    if vowels.count(a[0]) != 0:
        return word
    if len(a) == 1:
        return word
    if len(a) == 2:
        if vowels.count(a[1]) != 0:
            a =  a * number
            return word[0] + a[1:]
        else:
            return word
    if vowels.count(a[2]) != 0:
        if len(a) == 3:
            a = a[0:3] * number
            return word[0] + a[1:]
        else:
            a = a[0:3] * number + a[3:]
            return word[0] + a[1:]
    if vowels.count(a[1]) != 0:
        a = a[0:2] * number + a[2:]
        return word[0] + a[1:]
    return word
    
if __name__ == '__main__':
    pass