'''
Created on Sep 17, 2015

@author: Jonathan Yu
'''

def pigall(str):
    '''
    returns a piglatin-ized string
    of string parameter str
    '''
    all = []
    for word in str.split():
        all.append(pigword(word))
    return ' '.join(all)

def pigword(word):
    '''
    returns a piglatin-ized string
    of string parameter word
    '''
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    pigword = ""
    if len(word) == 1:
        #if word is one letter, appends "-way"
        pigword = word + "-way"
    elif word[0] in vowels:
        #if first letter of word is a vowel, appends "-way"
        pigword = word + "-way"
    else:
        '''
        if first letter of word is not a vowel,
        moves prefix before first vowel to end 
        with hyphen preceding the prefix and appends "ay"
        '''
        vowels.extend(("y", "Y"))
        firstVowel = ""
        for letter in word:
            #finding the first vowel in word
            if letter == word[0]:
                '''
                skips the first letter to avoid
                treating "y" at the beginning as
                a vowel (at this point, first
                letter is definitely not a vowel)
                '''
                continue
            if (letter.lower() == "u") & (word.find(letter) == 1):
                #if word starts with "qu", treats "u" like a non-vowel
                if word[word.find(letter) - 1].lower() == "q":
                    continue
            if letter in vowels:
                firstVowel = letter
                break
        if firstVowel == "":
            '''
            if no vowels in word, just treat it
            as if the first letter is a vowel
            (append "-way")
            '''
            pigword = word + "-way"
            return pigword
        pigword = word[word.find(firstVowel):] + "-" + word[:word.find(firstVowel)] + "ay" 
    return pigword

def unpigall(str):
    '''
    returns an unpiglatin-ized string
    of string paramater str
    '''
    all = []
    for word in str.split():
        all.append(unpigword(word))
    return ' '.join(all)

def unpigword(word):
    '''
    returns an unpiglatin-ized string
    of string parameter word
    '''
    unpigword = ""
    if word[len(word) - 4:] == "-way":
        #if word ends in "-way", removes those letters
        '''
        since multiple words can be transformed
        to the same pig-latin form with this ending,
        the function treats them all as words that
        begin with vowels
        '''
        unpigword = word[:len(word) - 4]
    elif word[len(word) - 2:] == "ay":
        '''
        if word ends in "ay", moves letters 
        after last hyphen but before "ay" to
        beginning and removes last hyphen and
        "ay"
        '''
        lastHyphen = 0
        for k in range(len(word) - 1, -1, -1):
            #finding the last hyphen by looping through word backwards
            if word[k] == "-":
                lastHyphen = k
                break
        unpigword = word[lastHyphen + 1:len(word) - 2] + word[:lastHyphen]
    return unpigword

def readFile(fname):
    '''
    returns a list of words read from file
    specified by fname
    '''
    f = open(fname)
    st = f.read()
    f.close()
    return st.split()

def writeFile(words, fname):
    '''
    write every element in words, a list of strings
    to the file whose name is fname
    put a space between every word written, and make
    lines have length 80
    '''
    LINE_SIZE = 80
    f = open(fname,"w")
    wcount = 0
    for word in words:
        f.write(word)
        wcount += len(word)
        if wcount + 1 > LINE_SIZE:
            f.write('\n')
            wcount = 0
        else:
            f.write(' ')
    f.close()
    
if __name__ == '__main__':
    # start with reading in data file
    words = readFile("romeo.txt")
    print "read",len(words),"words"
    result = ' '.join(words)
    # convert to piglatin and write to file
    pigstr = pigall(result)
    writeFile(pigstr.split(), "pig-romeo.txt")
    print "PIGIFIED romeo.txt"
    print pigstr[0:100]

    # read in pigified file
    words = readFile("pig-romeo.txt")
    print "read",len(words),"words"
    result = ' '.join(words)
    # unpigify file that was read
    unpigstr = unpigall(result)
    # write to file "unpig-romeo.txt"
    writeFile(unpigstr.split(), "unpig-romeo.txt")
    print "UNPIGIFIED romeo.txt"
    print unpigstr[0:100]
