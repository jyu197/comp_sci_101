'''
Created on Sep 15, 2015

@author: Jonathan Yu
'''

import random
import urllib2

def crawl(url):
    '''
    Parameter URL should be to a webpage that has
    links to all totem submissions, This function finds links
    to individual totem heads and returns a list of URLs, each
    URL references a different head from the webpage specified
    by parameter url
    '''
    page = urllib2.urlopen(url)
    source = page.read()
    start = 0
    lurls = []
    while True:
        index = source.find("href=",start)
        if index == -1:
            break
        endq = source.find('"',index+6)
        nurl = source[index+6:endq]
        if nurl.startswith("totem"):
            lurls.append(nurl)
        start = endq+1
        
    #create a list with full URLs foreach totem pole
    ret = []
    for tot in lurls:
        ret.append(url+"/"+tot)
    return ret

def randomPole(urlList, size):
    random.shuffle(urlList)
    urls = urlList[:size]
    for url in urls:
        source = urllib2.urlopen(url)
        st = source.read()
        print st

if __name__ == '__main__':
    mainUrl = "http://www.cs.duke.edu/courses/fall15/compsci101/assign/totem/uploads"
    data = crawl(mainUrl)
    randomPole(data, 5)