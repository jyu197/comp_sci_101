'''
Created on Dec 3, 2015

@author: Jonathan Yu
'''
import RecommenderEngine, json
import SimpleFoodReader
import BookReader

if __name__ == "__main__":
    (jitems,jratings) = BookReader.getData("bookratings.txt")
    #(jitems,jratings) = SimpleFoodReader.getData("foodratings_example.txt")
    
    items = json.loads(jitems)
    ratings = json.loads(jratings)
    
    avg = RecommenderEngine.averages(items,ratings)
    #just show book recommendations, not average ratings
    top = ", ".join([d[0] for d in avg[:5]])
    bottom = ", ".join([d[0] for d in avg[len(avg) - 5:]])
    print "The top recommendations are", top
    print "The bottom recommendations are", bottom
