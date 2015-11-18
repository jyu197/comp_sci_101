'''
Created on Nov 17, 2015

@author: Jonathan
'''

def findLabel(labels, deeds, needs):
    badges = []
    for i in range(len(needs)):
        earned = True
        for word in needs[i].split(" "):
            if word not in deeds:
                earned = False
        if earned:
            badges.append(labels[i])
    if len(badges) > 0:
        return badges[0]
    else:
        return "nobadge"

if __name__ == '__main__':
    pass