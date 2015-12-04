'''
Created on Dec 4, 2015

@author: Jonathan Yu
'''
import RecommenderEngine, json
import BookReader
import random

if __name__ == "__main__":
    (jitems,jratings) = BookReader.getData("bookratings.txt")
    
    items = json.loads(jitems)
    ratings = json.loads(jratings)
    
    name = ratings.keys()[random.randint(0, len(ratings) + 1)]
    count = 15
    recs = RecommenderEngine.recommend(name, items, ratings, count)
    recs = ", ".join(d[0] for d in recs[:10])
    print "Using " + str(count) + " other users' ratings, our top ten recommendations for " + name + " are " + recs + "."
    
    print
    
    name = ratings.keys()[random.randint(0, len(ratings) + 1)]
    count = 20
    recs = RecommenderEngine.recommend(name, items, ratings, count)
    recs = ", ".join(d[0] for d in recs[:10])
    print "Using " + str(count) + " other users' ratings, our top ten recommendations for " + name + " are " + recs + "."
