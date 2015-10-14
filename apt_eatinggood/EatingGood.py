'''
Created on Oct 13, 2015

@author: Jonathan Yu
'''

def howMany(meals, restaurant):
    num = 0
    people = []
    for meal in meals:
        data = meal.split(":")
        if data[1] == restaurant:
            if data[0] in people:
                continue
            num += 1
            people.append(data[0])
    return num

if __name__ == '__main__':
    pass