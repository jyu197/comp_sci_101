'''
Created on Sep 14, 2015

@author: Jonathan Yu
'''
from _ast import Num


def classAverage(data):
    grades = []
    for each in data:
        grades.append(float(each.split(";")[1]))
    return sum(grades)/len(grades)

def howManyInRange(data, year1, year2):
    years = []
    for each in data:
        years.append(int(each.split(";")[2]))
    num = 0;
    for year in years:
        if year >= year1:
            if year <= year2:
                num = num + 1
    return num

def process(name):
    f = open(name)
    answer = []
    for line in f:
        answer.append(line.strip())
    return answer          

if __name__ == '__main__':
    filename = "grades.txt"
    data = process(filename)
    for each in data:
        print each
    print
    print "Average grade is ", classAverage(data)
    year1 = 1991
    year2 = 1995
    print "Number born from ",year1,"to",year2,"is",
    print howManyInRange(data, year1, year2)
    