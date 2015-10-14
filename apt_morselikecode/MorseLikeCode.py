'''
Created on Sep 25, 2015

@author: Jonathan Yu
'''

def decrypt(library, message):
    encoded = message.split(" ")
    decoded = []
    for k in range(len(encoded)):
        for entry in library:
            if entry[2:] == encoded[k]:
                decoded.append(entry[0])
        if len(decoded) != k + 1:
            decoded.append("?")
    return "".join(decoded)

if __name__ == '__main__':
    pass