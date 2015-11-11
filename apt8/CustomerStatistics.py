'''
Created on Nov 10, 2015

@author: Jonathan
'''

def reportDuplicates(names):
    report = []
    for name in sorted(list(set(names))):
        occurences = names.count(name)
        if occurences > 1:
            report.append(name + " " + str(occurences))
    return report

if __name__ == '__main__':
    pass