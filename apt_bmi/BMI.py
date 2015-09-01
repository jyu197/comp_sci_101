'''
Created on Sep 1, 2015

@author: Jonathan Yu
'''

def calculate(weight,height):
    """
    return float indicating BMI
    (body mass index)
    given weight in pounds (float)
    given height in inches (float)
    """
    bmi = 703.0695 * weight / (height**2)
    return bmi

if __name__ == '__main__':
    print calculate(200, 60)