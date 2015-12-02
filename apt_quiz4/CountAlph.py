'''
Created on Dec 2, 2015

@author: Jonathan
'''

def summarize(words):
    return [str.lower("".join(words)).count(chr(i + 97)) for i in range(26)]

if __name__ == '__main__':
    pass