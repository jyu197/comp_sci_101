'''
Created on Sep 3, 2015

@author: Jonathan Yu
'''

def falling(time,velo):
    d = velo*time + 0.5*9.8*time**2
    return d

if __name__ == '__main__':
    print falling(3,5)
    print falling(3,0)
    print falling(3600,0)
    print falling(86400,0)