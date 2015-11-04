'''
Created on Nov 4, 2015

@author: Jonathan
'''

def green(pixels):
    greens = []
    for pixel in pixels:
        values = pixel.split(",")
        if int(values[1]) > int(values[0]) + int(values[2]):
            greens.append(pixels.index(pixel))
    return greens

if __name__ == '__main__':
    pass