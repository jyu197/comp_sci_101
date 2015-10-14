'''
Created on Sep 21, 2015

@author: Jonathan Yu
'''

def getMessage(original):
    words = original.split(" ")
    vowels = ["a", "e", "i", "o", "u"]
    onlyVowels = True
    message = ""
    for word in words:
        letters = list(word)
        for k in range(len(letters)):
            if letters[k] not in vowels:
                onlyVowels = False
                if (k > 0) & (letters[k - 1] not in vowels):
                    letters[k] = "0"
        if onlyVowels == False:
            for k in range(len(letters)):
                if letters[k] in vowels:
                    letters[k] = "0"
        onlyVowels = True
        for letter in letters:
            message = message + letter
        message = message + " "
    message = message.replace("0","")
    return message.strip()

if __name__ == '__main__':
    pass