'''
Created on Nov 10, 2015

@author: Jonathan
'''

def emailsLargest(courses):
    sizes = {}
    for course in sorted(courses):
        name = course.split(":")[0]
        if name not in sizes:
            sizes[name] = 0
        else:
            sizes[name] += 1
    largest = max(sorted(sizes), key = sizes.get)
    emails = []
    for course in sorted(courses):
        data = course.split(":")
        if data[0] == largest:
            emails.append(data[2])
    return " ".join(emails)

if __name__ == '__main__':
    pass