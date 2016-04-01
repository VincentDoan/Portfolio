__author__ = 'Ryan'

#string = "http:::::::::;;wwwNIGNOGEDU"
#string += ".txt"
#f = open(string, 'w+')
#f.write("YO BRO")
#f.close()

#f = open("Count.txt", 'r')
#count = int(f.readline())
#count = count + 1
#print count
#f.close()
#f = open("Count.txt", "w")
#f.write("%s" % count)
#f.close()

#hash = {}
#count = 1
#f = open("Count.txt", "r+")
#if f.readline() is "":
#  count = 1
#else:
#print hash.__len__()

import os
class Page(object):
    def __init__(self, url, rank, term):
        self.url = url
        self.rank = rank
        self.term = term

def wordsToHash(hash, words, id):
    #checks if words are in stopword hash, adds if it isn't. DOES NOT ADD random apostrophes and hyphens
    if (words.__sizeof__() >  0):
        for item in words:
           if (item == "'" or item == "-" or item.isdigit() or item.__len__() < 3):
               pass
           else:
            if not (item in hash):
                page = Page(id, 1, item)
                urlHash = {}
                urlHash[id] = page
                hash[item] = urlHash
            else:
                if (id not in hash[item]):
                    page = Page(id, 1, item)
                    urlHash = {}
                    urlHash[id] = page
                    hash[item].update(urlHash)
                else:
                    hash[item][id].rank =str(int(hash[item][id].rank) + 1)


def getTerms(hash):
    string = ""
    stopwords = {"a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", \
                 "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", \
                 "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", \
                 "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", \
                 "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", \
                 "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", \
                 "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", \
                 "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", \
                 "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", \
                 "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", \
                 "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", \
                 "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "through", "to", "too", \
                 "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", \
                 "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", \
                 "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", \
                 "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"}

    #parses alphanumeric strings without empty lines allows apostrophe and hypens

    with open("ID.txt") as f1:
        if (os.stat("ID.txt").st_size != 0):
            for line in f1:
                words = []
                id = line.split("\t")
                id[id.__len__() - 1] = id[id.__len__() - 1].strip()
                with open(id[0] + ".txt") as f:
                    while True:
                        c = f.read(1).lower()
                        if ((c.isalpha() or c.isdigit() or c == "'" or c == "-")): #hyphenated words separate token
                            string += c.lower()
                        elif not string == '':
                            if string in stopwords:
                                string = ""
                            else:
                              words.append(string)
                              string = ""
                        if not c:
                            break
                wordsToHash(hash, words, id[1])

                f.close()
    f1.close()

hash = {}

with open("YO.txt") as f:
    if (os.stat("YO.txt").st_size != 0):
        for line in f:
            urlHash = {}
            string = line.split("\t")
            string[string.__len__() - 1] = string[string.__len__() - 1].strip()
            page = Page(string[1], string[2], string[0])
            urlHash[string[1]] = page
           # for x in range(1, string.__len__()):


            hash[string[0].lower()] = urlHash
    f.close()
   # for x in hash.keys():
     #   string = x + "\t"
      #  for y in hash[x].keys():
       #   print string + y + "\t" + str(hash[x][y].rank)

    getTerms(hash)

f = open("YO2.txt", "w")
for x in hash.keys():
    list = []
    string = x + "\t"
    for y in hash[x].keys():
        list.append(hash[x][y])
    list.sort(key=lambda x: int(x.rank), reverse=True)
    for z in list:
        f.write (x + "\t" + z.url + "\t" + str(z.rank) + "\n")

#f = open("YO2.txt", "w")
#for x in hash.keys():
 #       string = x + "\t"
  #      for y in hash[x].keys():
   #       f.write(string + y + "\t" + str(hash[x][y].rank) + "\n")
#for x in hash.keys():
   # f.write (x + "\t" + str(hash[x].keys()) + "\n")
   # f.write(hash[x])
f.close()

term = raw_input("Enter in a search term: ").lower()
list = []
for x in hash[term].keys():
     list.append(hash[term][x])
list.sort(key=lambda x: int(x.rank), reverse=True)
for x in list:
    print (x.url + "\t" + str(x.rank))