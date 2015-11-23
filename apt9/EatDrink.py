'''
Created on Nov 23, 2015

@author: Jonathan
'''

import operator

def winners(data):
    tasks = {}
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        time = data[i][1].split(":")
        data[i][1] = int(time[0]) * 60 + int(time[1])
        name = data[i][0]
        time = data[i][1]
        if name not in tasks:
            tasks[name] = []
        tasks[name].append(time)
    sortData = []
    for name in tasks:
        sortData.append([name, len(tasks[name]), sum(tasks[name])])
    sortData.sort(key = operator.itemgetter(2))
    sortData.sort(key = operator.itemgetter(1), reverse = True)
    return [entry[0] for entry in sortData]
         
if __name__ == '__main__':
    pass