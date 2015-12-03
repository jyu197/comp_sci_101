'''
Created on Dec 2, 2015

@author: Jonathan
'''

def edit(entry):
    entry = [set(words.split(" ")) for words in entry]
    edited = False
    while not edited:
        edited = True
        for i in range(len(entry)):
            for k in range(len(entry)):
                if k == i:
                    continue
                if len(entry[i] & entry[k]) >= 2:
                    entry.append(entry[i] | entry[k])
                    entry[i] = set("")
                    entry[k] = set("")
                    edited = False
        entry = [words for words in entry if words != set("")]
    return sorted([" ".join(sorted(list(words))) for words in entry])   

if __name__ == '__main__':
    pass