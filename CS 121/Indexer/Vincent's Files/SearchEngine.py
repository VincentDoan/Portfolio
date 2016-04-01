__author__ = 'Vincent'

import linecache
import os

class Page(object):
    def __init__(self, url, term, rank):
        self.url = url
        self.term = term
        self.rank = rank


#Term to Page Object
dict = {}

dict2 = {}
dict4 = {}

with open("dict2.txt") as f:
    if (os.stat("dict2.txt").st_size != 0):
        for line in f:
            string = line.split("\t")
            string[string.__len__() - 1] = string[string.__len__() - 1].strip()
            list = []
            for x in range(1, string.__len__()):
                list.append(string[x])
            dict2[string[0]] = list

with open("dict4.txt") as f:
    if (os.stat("dict4.txt").st_size != 0):
        for line in f:
            string = line.split("\t")
            string[string.__len__() - 1] = string[string.__len__() - 1].strip()
            list = []
            for x in range(1, string.__len__()):
                list.append(string[x])
            dict4[string[0]] = list

#Our search engine list, sorted by rank
search = []
dict = {}

#f2 = open("dict.txt", "w")

with open("dict6.txt") as f:
    if (os.stat("dict6.txt").st_size != 0):
        for line in f:
            string = line.split("\t")
            string[string.__len__() - 1] = string[string.__len__() - 1].strip()
            page = Page(string[0], string[1], string[2])
            if string[1] not in dict.keys():
                list = [page]
                dict[string[1]] = list
            else:
                dict[string[1]].append(page)

           #for x in range(1, string.__len__()):
            #    list.append(string[x])
            #dict6[string[0]] = list

term = raw_input("Enter in a search term: ")#.lower()
for x in dict[term]:
     search.append(x)
search.sort(key=lambda x: x.rank, reverse=True)
for x in search:
    print (x.url + "\t" + str(x.rank))
    #print(linecache.getline("CommonWords.txt", 33))
'''
with open("dict2.txt") as f:
    if (os.stat("dict2.txt").st_size != 0):
        for line in f:
            string = line.split("\t")
            string[string.__len__() - 1] = string[string.__len__() - 1].strip()
            list = []
            for x in range(1, string.__len__()):
                list.append(string[x])
            dict2[string[0]] = list

with open("dict4.txt") as f:
    if (os.stat("dict4.txt").st_size != 0):
        for line in f:
            string = line.split("\t")
            string[string.__len__() - 1] = string[string.__len__() - 1].strip()
            list = []
            for x in range(1, string.__len__()):
                list.append(string[x])
            dict4[string[0]] = list


with open("dict6.txt") as f:
    if (os.stat("dict6.txt").st_size != 0):
        for line in f:
            string = line.split("\t")
            string[string.__len__() - 1] = string[string.__len__() - 1].strip()
           # hash[""]
            #print string

                #page = Page(string[1], string[2], string[0])
                #urlHash[string[1]] = page
'''
