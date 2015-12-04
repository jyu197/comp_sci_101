'''
Created on Nov 24, 2015

@author: ola
'''
import RecommenderEngine, json
import SimpleFoodReader
import BookReader
import MovieReader

if __name__ == "__main__":
    #(jitems,jratings) = SimpleFoodReader.getData("foodratings_example.txt")
    (jitems,jratings) = BookReader.getData("bookratings.txt")
    #(jitems,jratings) = MovieReader.getData("movieratings.txt")
    print "items = ",jitems
    print "ratings = ", jratings
    
    items = json.loads(jitems)
    ratings = json.loads(jratings)
    
    avg = RecommenderEngine.averages(items,ratings)
    print avg
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        print key,slist
        print "\t",RecommenderEngine.scores(slist,items,ratings,1)
        print "\t",RecommenderEngine.scores(slist,items,ratings,len(slist))
        
    print RecommenderEngine.recommend(ratings.keys()[0], items, ratings, 5)
    #for the above test, I randomly chose a name and a count
