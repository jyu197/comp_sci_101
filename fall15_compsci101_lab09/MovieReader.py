'''
Created on Nov 8, 2015

@author: Jonathan
'''

import csv

def readandprocess(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    datad = {}
    freader.next()
    #numUS = 0
    for row in freader:
        '''
        if "US" in row[3].split("-"):
            numUS += 1
        '''
        year = row[1]
        title = row[2]
        if int(year) < 1940:
            continue
        decade = year[2] + "0's"
        if decade not in datad:
            datad[decade] = [title]
        else:
            datad[decade].append(title)
        '''
    print numUS
    '''
    info = datad.items()
    tosort = [(t[0], len(t[1])) for t in info]
    print sorted(tosort)

if __name__ == '__main__':
    readandprocess("9600movies.csv")