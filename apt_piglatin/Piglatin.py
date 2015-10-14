'''
Created on Sep 21, 2015

@author: Jonathan Yu
'''

def convert(s):
    vowels = ["a","e","i","o","u"]
    if s[0] in vowels:
        return s + "-way"
    elif s[0] == "q":
        return s[2:] + "-quay"
    else:
        for letter in s:
            if letter in vowels:
                return s[s.find(letter):] + "-" + s[0:s.find(letter)] + "ay"

if __name__ == '__main__':
    pass