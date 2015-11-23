'''
Created on Nov 16, 2015

@author: ola
'''

import Replacements

def printStory(st):
    size = 60
    current = 0
    for w in st.split():
        if current + len(w) >= size:
            print
            print w + " ",
            current = len(w) + 1
        else:
            current += len(w) + 1
            print w+" ",
    print 

def readtemplate(fname):
    '''
    read file specified by fname
    and return list of all words in fname
    '''
    f = open(fname)
    st = f.read()
    data = st.split()
    
    f.close()
    return data

def makeStory(words):
    story = ""
    for w in words:
        if w.find("<") != -1:
            start = w.find("<")
            end = w.find(">")
            prefix = w[:start]
            suffix = w[end+1:]   
            tag = w[start+1:end]
            rep = Replacements.getReplacement(tag)
            story = story + prefix + rep + suffix + " "  
        else:
            story = story + w + " "
    return story.strip()

if __name__ == '__main__':
    words = readtemplate("templates/mytemplate1.txt")
    st = makeStory(words)
    printStory(st)
    print
    words = readtemplate("templates/mytemplate2.txt")
    st = makeStory(words)
    printStory(st)
