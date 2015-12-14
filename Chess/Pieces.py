'''
Created on Dec 6, 2015

@author: Jonathan Yu
'''

class Pawn:
    
    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos
    
    def move(self):
        self.pos[1] += 1

if __name__ == '__main__':
    pass