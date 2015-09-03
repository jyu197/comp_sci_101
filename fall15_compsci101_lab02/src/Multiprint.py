'''
Date: Sept 2-3, 2015

@author: YOUR NAME HERE
'''


word = "wonderful"
count = 1

def printit():
    global count,word
    print count,"\t",word
    count = count + 1
def f1():
    f2()
    f2()
    f2()
    f2()

def f2():
    f3()
    f3()
    f3()
    f3()

def f3():
    printit()
    printit()
    printit()
    printit()
    
    
def verse():
    f1()
    f1()
    f1()
    f1()
    
if __name__ == "__main__":
    verse()
    