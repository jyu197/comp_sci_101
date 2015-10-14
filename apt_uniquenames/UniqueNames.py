'''
Created on Oct 13, 2015

@author: Jonathan Yu
'''

def namesForYear(courses, year):
    names = []
    for course in courses:
        roster = course.split(":")
        for k in range(2, len(roster), 2):
            if roster[k] == year:
                names.append(roster[k - 1])
    return " ".join(sorted(set(names)))

if __name__ == '__main__':
    pass