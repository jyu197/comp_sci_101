'''
Created on Dec 3, 2015

@author: Jonathan Yu
'''

from operator import itemgetter

def averages(items, ratings):
    """
    returns a list that represents item recommendations computed by
    averaging item-by-item ratings
    """
    avgs = []
    for i in range(len(items)):
        avgs.append((items[i], getAverage(i, ratings)))
    avgs.sort(key = itemgetter(0))
    avgs.sort(key = itemgetter(1), reverse = True)
    return avgs
        
def getAverage(index, ratings):
    """
    returns the average of the ratings at index within the value lists
    of dictionary ratings
    """
    sumRatings = 0.0
    raters = len(ratings) + 1
    for rater in ratings:
        rating = ratings[rater][index]
        if rating == 0:
            raters -= 1
            continue
        sumRatings += rating
    return sumRatings / raters

def similarities(name, ratings):
    """
    returns a list of per-user similarities of each user/rater to the 
    user/rater whose name is a parameter
    """
    sim = []
    for rater in ratings:
        if rater == name:
            continue
        sim.append((rater, getDotProduct(name, rater, ratings)))
    sim.sort(key = itemgetter(0))
    sim.sort(key = itemgetter(1), reverse = True)
    return sim
        
def getDotProduct(name, rater, ratings):
    """
    returns the dot-product of the value lists for keys, name and rater,
    within ratings
    """
    dot = 0
    for i in range(len(ratings[name])):
        dot += ratings[name][i] * ratings[rater][i]
    return dot

def scores(slist, items, ratings, n):
    """
    returns a list of recommendations calculated for a specific user/rater by
    weighing user ratings more heavily for users close to the specific user
    """
    scrs = []
    weighted = [0] * len(items)
    for i in range(n):
        rater = slist[i][0]
        sim = slist[i][1]
        rating = ratings[rater]
        weighted = addRatings(weighted, weight(rating, sim))
    for i in range(len(weighted)):
        scrs.append((items[i], weighted[i]))
    scrs.sort(key = itemgetter(0))
    scrs.sort(key = itemgetter(1), reverse = True)
    return scrs

def weight(rating, sim):
    """
    weights a rater's ratings based off that rater's similarity index
    """
    weighted = []
    for num in rating:
        weighted.append(num * sim)
    return weighted

def addRatings(sumRatings, rating):
    """
    adds a set of ratings to an accumulator
    """
    newSum = []
    for i in range(len(sumRatings)):
        newSum.append(sumRatings[i] + rating[i])
    return newSum

def recommend (name, items, ratings, count):
    """
    returns a list of recommendations calculated for a specific user/rater
    """
    recs = []
    for i in range(len(ratings[name])):
        if ratings[name][i] != 0:
            continue
        item = items[i]
        slist = similarities(name, ratings)
        scrs = scores(slist, items, ratings, count)
        for scr in scrs:
            if scr[0] == item:
                score = scr[1]
        if score <= 0:
            continue
        avrges = averages(items, ratings)
        for avrge in avrges:
            if avrge[0] == item:
                average = avrge[1]
        recs.append((item, score, average))
    recs.sort(key = itemgetter(0))
    recs.sort(key = itemgetter(1), reverse = True)
    return recs

if __name__ == '__main__':
    pass
