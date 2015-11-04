'''
Created on Nov 4, 2015

@author: Jonathan
'''

def check(word):
    replaced = word.replace("pi", "0")
    replaced = replaced.replace("ka", "0")
    replaced = replaced.replace("chu", "0")
    replaced = replaced.replace("0", "")
    if replaced == "":
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    pass