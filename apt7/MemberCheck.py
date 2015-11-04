'''
Created on Nov 4, 2015

@author: Jonathan
'''

def whosDishonest(club1, club2, club3):
    names1 = set(club1)
    names2 = set(club2)
    names3 = set(club3)
    return sorted(set((names1 & names2) | (names1 & names3) | (names2 & names3)))
        

if __name__ == '__main__':
    pass