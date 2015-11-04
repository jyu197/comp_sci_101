'''
Created on Nov 4, 2015

@author: Jonathan
'''

def networth(transactions):
    flows = {}
    for transaction in transactions:
        data = transaction.split(":")
        if data[0] not in flows:
            flows[data[0]] = 0
        if data[1] not in flows:
            flows[data[1]] = 0
        flows[data[0]] -= float(data[2])
        flows[data[1]] += float(data[2])
    flowsList = []
    for flow in flows:
        flowsList.append(flow + ":" + str(flows.get(flow)))
    return sorted(flowsList)

if __name__ == '__main__':
    pass