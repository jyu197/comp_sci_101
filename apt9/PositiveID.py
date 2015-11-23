'''
Created on Nov 23, 2015

@author: Jonathan
'''

def maximumFacts(suspects):
    most = 0
    for i in range(len(suspects)):
        suspects[i] = suspects[i].split(",")
    for i in range(len(suspects)):
        for j in range(len(suspects)):
            if i == j:
                continue
            common = len(set(suspects[i]) & set(suspects[j]))
            if common > most:
                most = common
    return most

if __name__ == '__main__':
    pass