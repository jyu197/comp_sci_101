'''
Created on Nov 4, 2015

@author: Jonathan
'''

def combine(foreground, background):
    for pixel in foreground:
        values = pixel.split(",")
        if int(values[1]) > int(values[0]) + int(values[2]):
            index = foreground.index(pixel)
            foreground[index] = background[index]
    return foreground

if __name__ == '__main__':
    pass