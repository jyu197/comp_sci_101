'''
Created on Oct 10, 2015

@author: Jonathan Yu
'''

def theMin(room):
    changes = 0
    changed = list(room)
    for k in range(1, len(changed) - 1):
        if changed[k - 1] == changed[k] == changed[k + 1]:
            changed[k] = "CHANGED"
            changes += 1
    for k in range(len(changed) - 1):
        if changed[k] == changed[k + 1]:
            changes += 1
    return changes

if __name__ == '__main__':
    pass