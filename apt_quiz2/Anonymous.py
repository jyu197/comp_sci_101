'''
Created on Nov 3, 2015

@author: Jonathan
'''

def howMany(headlines, messages):
    howMany = 0
    for message in messages:
        headlinesLetters = list("".join(headlines).lower())
        messageLetters = "".join(message.split()).lower()
        writeable = True
        for letter in messageLetters:
            if letter in headlinesLetters:
                headlinesLetters.remove(letter)
            else:
                writeable = False
        if writeable:
            howMany += 1
    return howMany

if __name__ == '__main__':
    pass