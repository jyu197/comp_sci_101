'''
Created on Nov 23, 2015

@author: Jonathan
'''

import operator

def generate(results):
    medals = {}
    for result in results:
        for i in range(3):
            country = result.split(" ")[i]
            if country not in medals:
                medals[country] = [0, 0, 0]
            medals[country][i] += 1
    table = []
    for country in medals:
        table.append([country] + medals[country])
    table.sort(key = operator.itemgetter(0))
    table.sort(key = operator.itemgetter(3), reverse = True)
    table.sort(key = operator.itemgetter(2), reverse = True)
    table.sort(key = operator.itemgetter(1), reverse = True)
    for i in range(len(table)):
        table[i] = " ".join([str(j) for j in table[i]])
    return table

if __name__ == '__main__':
    pass