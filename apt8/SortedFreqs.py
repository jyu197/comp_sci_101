'''
Created on Nov 10, 2015

@author: Jonathan
'''

def freqs(data):
    frequencies = []
    for word in sorted(list(set(data))):
        frequencies.append(data.count(word))
    return frequencies

if __name__ == '__main__':
    pass