'''
Version 2 on November 1, 2015

Original: Oct 24, 2012

@author: ola
'''

import csv

def readandprocess(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    datad = {}
    header = freader.next()
    #print "header row labels",header
    for row in freader:
        #print row
        artist = row[2]
        song = row[1]
        if artist not in datad:
            datad[artist] = [song]
        else:
            datad[artist].append(song)
        '''
        if artist == "Beatles":
            print "Beatles title: ",row[1]
        '''
    '''
    for artist in datad:
        print artist, datad[artist]
    '''
    '''
    info = datad.items()
    tosort = [(len(t[1]), t[0]) for t in info]
    info = sorted(tosort)
    print info[-30:]
    '''
    info = datad.items()
    wordCount = {}
    for entry in info:
        for title in entry[1]:
            words = set(title.split(" "))
            for word in words:
                if len(word) <= 3:
                    continue
                if word not in wordCount:
                    wordCount[word] = 1
                else:
                    wordCount[word] += 1
    info = wordCount.items()
    tosort = [(t[1], t[0]) for t in info]
    info = list(reversed(sorted(tosort)))
    print info[0][1]

  
if __name__ == '__main__':
    readandprocess("top1000.csv")
