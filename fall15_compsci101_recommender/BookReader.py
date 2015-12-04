'''
Created on Dec 3, 2015

@author: Jonathan Yu
'''

import json

def readDatafile (filename):
    """
    given a filename that is formatted as comma separated values,
    return a list of lists of strings, where each line is represented
      as a list of separate string elements
    """
    f = open(filename)
    result = [ line.strip().split(',') for line in f.readlines() if len(line) > 1 ]
    f.close()
    return result


# HELPER FUNCTION
def convertStrings (statList):
    """
    given a list of strings representing int values,
      return a list of ints, the converted values of the strings
    """
    return [ int(s) for s in statList ]


# PRIMARY MODULE FUNCTION
def getData (filename):
    """
    given the name of a file of data about book ratings, 
      returns two sequences: a list of strings, the book names in file order,
      and a dictionary of strings as the key and a list of ints as the values, the
      raters and their ratings of the books
    """
    data = readDatafile(filename)
    
    """
    book names are the strings at odd indices in the list of string elements that 
    represent one line (each line has the same books)
    """
    itemList = [ book for book in data[0] if data[0].index(book) % 2 != 0 ]
    
    """
    ratings are the strings at even indices (except for 0)in the list of string
    elements that represent one line
    """
    ratingsDict = {}
    for line in data:
        rater = line[0]
        ratings = convertStrings([rating for rating in line if line.index(rating) % 2 == 0][1:])
        ratingsDict[rater] = ratings
    return (json.dumps(itemList), json.dumps(ratingsDict))

if __name__ == "__main__":
    (items,ratings) = getData("bookratings.txt")
    print"items = ",items
    print"ratings = ", ratings
    
    print type(items), type(ratings)
    var = json.loads(items)
    print type(var),var
    dvar = json.loads(ratings)
    print type(dvar),dvar
