'''
Created on Sep 1, 2014

@author: ola
'''

def eieio():
    print "Ee-igh, Ee-igh, oh!"
    
def refrain():
    print "Old MacDonald had a farm,",
    eieio()

def had_a(animal):
    print "And on his farm he had a",animal,",",
    eieio()

def with_a(noise):
    print "With a",noise,noise,"here"
    print "And a", noise, noise, "there"
    print "Here a",noise, "there a",noise,"everywhere a",noise,noise

    
def pig():
    refrain()
    had_a("pig")
    with_a("oink")
    refrain()
    
def fox():
    refrain()
    had_a("fox")
    with_a("ringdingding")
    
    
if __name__ == '__main__':
    pig()
    print
    fox()
    print