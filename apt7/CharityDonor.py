'''
Created on Nov 4, 2015

@author: Jonathan
'''

def nameDonor(contributions):
    donations = {}
    for contribution in contributions:
        data = contribution.split(":")
        if data[0] not in donations:
            donations[data[0]] = 0
        donations[data[0]] += float(data[1])
    largest = 0
    mostGenerous = ""
    for donation in sorted(donations):
        if donations.get(donation) > largest:
            largest = donations.get(donation)
            mostGenerous = donation
    return mostGenerous        

if __name__ == '__main__':
    pass