'''
Created on Oct 13, 2015

@author: Jonathan Yu
'''

def getFortunate(a, b, c):
    sums = []
    for i in a:
        for j in b:
            for k in c:
                sums.append(i + j + k)
    num = 0
    for sum in set(sums):
        isFortunate = True
        for digit in str(sum):
            if not ((digit == "5") | (digit == "8")):
                isFortunate = False
                break
        if isFortunate:
            num += 1
    return num
            
if __name__ == '__main__':
    pass