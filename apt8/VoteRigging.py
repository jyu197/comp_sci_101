'''
Created on Nov 8, 2015

@author: Jonathan
'''

def minimumVotes(votes):
    changes = 0
    while max(votes) != votes[0] :
        changes += 1
        votes[votes.index(max(votes))] -= 1
        votes[0] += 1
    if votes.count(votes[0]) != 1:
        changes += 1
    return changes

if __name__ == '__main__':
    pass