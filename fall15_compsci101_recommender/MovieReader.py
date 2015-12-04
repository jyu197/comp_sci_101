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


# PRIMARY MODULE FUNCTION
def getData (filename):
    """
    given the name of a file of data about movie ratings, 
      returns two sequences: a list of strings, the movie names in file order,
      and a dictionary of strings as the key and a list of ints as the values, the
      raters and their ratings of the movies
    """
    data = readDatafile(filename)
    
    """
    movie names are the strings at index 1 in each list of string elements that
    represent one line
    since the ratings in the file are in no particular order, must make sure each
    movie only appears once in itemList
    """
    itemList = list(set([ d[1] for d in data ]))
    
    """
    ratings are the strings at index 2 in each list of string elements that represent
    one line
    """
    ratingsDict = {}
    for line in data:
        """
        since the ratings in the file are in no particular order, must initialize each
        value in the dictionary as an empty list with the same length as itemList
        then, as the file is processed, update the dictionary so that the index of the
        rating corresponds to the index of the matching movie in itemList
        """
        rater = line[0]
        if rater not in ratingsDict:
            ratingsDict[rater] = [0] * len(itemList)
        rating = int(line[2])
        ratingsDict[rater][itemList.index(line[1])] = rating
    return (json.dumps(itemList), json.dumps(ratingsDict))

if __name__ == "__main__":
    (items,ratings) = getData("movieratings.txt")
    print"items = ",items
    print"ratings = ", ratings
    
    print type(items), type(ratings)
    var = json.loads(items)
    print type(var),var
    dvar = json.loads(ratings)
    print type(dvar),dvar
