'''
Created on Nov 23, 2015

@author: Jonathan
'''

def bestInvitation(first, second):
    most = 0
    for interest in (first + second):
        shares = first.count(interest) + second.count(interest)
        if shares > most:
            most = shares
    return most

if __name__ == '__main__':
    pass