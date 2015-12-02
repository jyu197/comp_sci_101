'''
Created on Dec 2, 2015

@author: Jonathan
'''

def highestScore(friends):
    most = 0
    for i in range(len(friends)):
        twoFriends = []
        for k in range(len(friends[i])):
            if friends[i][k] == "Y":
                twoFriends.append(k)
                for l in range(len(friends[k])):
                    if l == i:
                        continue
                    if (friends[k][l] == "Y") & (friends[i][l] == "N"):
                        twoFriends.append(l)
        if len(set(twoFriends)) > most:
            most = len(set(twoFriends))
    return most

if __name__ == '__main__':
    pass