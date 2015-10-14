'''
Created on Sep 21, 2015

@author: Jonathan Yu
'''

def decode(cipher, shift):
    decoded = ""
    for letter in cipher:
        newValue = ord(letter) - shift
        if newValue < 65:
            newValue = 91 - (65 - newValue)
        decoded = decoded + chr(newValue)
    return decoded
    
if __name__ == '__main__':
    pass