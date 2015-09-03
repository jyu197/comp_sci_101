'''
Date: Sept 2-3, 2015

@author: Jonathan Yu
'''

def first_verse():
    dell()
    dell()
    hiho()
    dell()
    print
    
def verse(taker,thing):
    print "And the " + taker + " takes the " + thing
    take(taker,thing)
    hiho()
    take(taker,thing)
    print

def last_verse():
    print "And the cheese stands alone"
    alone()
    hiho()
    alone()
    
def dell():
    print "The farmer in the dell"

def hiho():
    print "Hi-ho, the derry-o"

def take(taker,thing):
    print "The " + taker + " takes the " + thing
    
def alone():
    print "The cheese stands alone"

def song():
    first_verse()
    verse("farmer","wife")
    verse("wife","child")
    verse("child","nurse")
    verse("nurse","dog")
    verse("dog","cat")
    verse("cat","mouse")
    verse("mouse","cheese")
    last_verse()

if __name__ == '__main__':
    song()
