'''
Created on Sep 28, 2015

@author: Jonathan Yu
'''

def getAgeList(filename, low, high):
    file = open(filename)
    list = []
    for line in file:
        entry = line.split(",")
        if low <= int(entry[2]) <= high:
            list.append(entry[0])
    return list

if __name__ == '__main__':
    print getAgeList("data.txt", 15, 30)
    print getAgeList("data.txt", 70, 100)
    print getAgeList("data.txt", 1, 8)