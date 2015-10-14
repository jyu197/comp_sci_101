'''
Created on Sep 23, 2015

@author: Jonathan Yu
'''

def encrypt(str, shift):
    '''
    returns an encrypted string
    of string parameter str
    '''
    all = []
    for word in str.split():
        all.append(shiftword(word, shift))
    return ' '.join(all)

def shiftword(word, shift):
    '''
    returns an encrypted string
    of string parameter word
    '''
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caesar = alph[shift:] + alph[:shift]
    shifted = ""
    for letter in word:
        #shifts each letter by a value of int parameter shift
        #this function respects the case of parameter word
        if letter.islower():
            alph = alph.lower()
            caesar = caesar.lower()
        else:
            alph = alph.upper()
            caesar = caesar.upper()
        if letter.isalpha():
            shifted = shifted + caesar[alph.find(letter)]
        else:
            shifted = shifted + letter
    return shifted

def eyeball(encrypted):
    '''
    prints all shifted possibilities
    of string parameter encrypted
    '''
    for k in range(26):
        print str(k) + " " + encrypt(encrypted, k)[:80]

def chisquare(encrypted):
    '''
    returns the shift value that generates
    the minimum chi-square value when
    decrypting string parameter encrypted
    '''
    lowest = float("inf")
    shift = 0
    for k in range(26):
        #calculates the chi-square value for each possible shift
        freqs = [8.04, 1.48, 3.34, 3.82, 12.49, 2.40, 1.87, 5.05,  7.57, 
             0.16, 0.54, 4.07, 2.51, 7.23, 7.64, 2.14, 0.12, 6.28,
             6.51, 9.28, 2.73, 1.05, 1.68, 0.23, 1.66, 0.09]
        shifted = encrypt(encrypted, k)
        actualCounts = alphaFreq(shifted)
        expectedCounts = []
        numAlpha = 0
        for letter in encrypted:
            '''
            determining the number of alphabetic
            characters in parameter encryped
            '''
            if letter.isalpha():
                numAlpha = numAlpha + 1
        for freq in freqs:
            #calculating the expected count for each letter
            expectedCounts.append(freq / 100.0 * numAlpha)
        differences = []
        for l in range(len(actualCounts)):
            '''
            calculating the difference between
            the expected and actual count of
            each letter
            '''
            differences.append(expectedCounts[l] - actualCounts[l])
        chisquare = 0
        for l in range(len(differences)):
            chisquare = chisquare + ((differences[l] ** 2) / expectedCounts[l])
        if chisquare < lowest:
            #finding the lowest chi-square value and its shift
            lowest = chisquare
            shift = k
    return shift

def alphaFreq(str):
    '''
    returns a list of counts of the letters
    in string parameter str
    '''
    counts = [0] * 26
    for letter in str:
        if not letter.isalpha():
            continue
        dex = ord(letter.lower()) - ord("a")
        counts[dex] = counts[dex] + 1
    return counts

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
    print "Encrypting romeo with a Caesar cypher of 19"
    encrypted = encrypt(" ".join(readFile("romeo.txt")), 19).split(" ")
    writeFile(encrypted, "crypt-romeo.txt")
    print " ".join(encrypted)[:80]
    
    print "\n" + "Eyeballing from file1"
    eyeball(" ".join(readFile("file1.txt")))

    print "\n" + "Chi-square decrypting file2"
    encrypted = " ".join(readFile("file2.txt"))
    chisquare = chisquare(encrypted)
    print chisquare
    print encrypt(encrypted, int(chisquare))[:80]
