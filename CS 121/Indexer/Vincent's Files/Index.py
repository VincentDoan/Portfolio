import json
import os
from pprint import pprint
import re
import math as math

def hasNumbers(string):
    return any(char.isdigit() for char in string)

class Page(object):
    def __init__(self, id, url, title, term, rank):
        self.id = id
        self.url = url
        self.title = title
        self.term = term
        self.rank = rank


#Change path to directory where website files are
path = r'C:\Users\Ryan\PycharmProjects\Test\json'
i = 0
#ID:[Words]
dict1 = {}
#Word:[IDs]
dict2 = {}
#URL:ID
dict3 = {}
#ID:title
dict4 = {}
#ID:#Words
dict5 = {}
#ID:[ Word:TF-IDF ]
dict6 = {}

replacer = re.compile('[1234567890]')
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

for file in os.listdir(path): #enter directory
    #opens file
    file_name = str(i) + '.txt'
    data_file = open(os.path.join(path, file_name),'r')
    string = data_file.read()
    raw_file = json.loads(string)

    print(i)

    i = i+1

    #finds URL, body, and id
    URL = raw_file["_id"].encode('utf-8')
    body = raw_file["text"].encode('utf-8')
    id = int(raw_file["id"])
    dict1[URL] = []
    dict3[URL] = id
    dict4[URL] = replacer.sub('', raw_file["title"].encode('utf-8'))
    dict5[URL] = 0
    dict6[URL] = {}

    #if the current word is not a key in dict1, add it with an empty list
    #if the current word is not the the current URLs list, add it
    #it the current URL is not in the current word's list, add it
    for word in body.split():
        dict5[URL] = dict5[URL]+1
        replacer.sub('', word)
        word = word.lower().encode('utf-8')
        if word.lower() not in stopwords and not hasNumbers(word.lower()) and len(word) >= 3:
            if not word in dict2:
                dict2[word.encode('utf-8')] = []
            if word not in dict1[URL]:
                dict1[URL].append(word.encode('utf-8'))
            if URL not in dict2[word]:
                dict2[word.encode('utf-8')].append(URL)
            if word in dict6[URL]:
                dict6[URL][word] = dict6[URL][word] + 1
            else:
                dict6[URL][word] = 1

for URL in dict6:
    for word in dict6[URL]:
        TF = float(dict6[URL][word]) / float(dict5[URL])
        IDF = math.log(49956 / int( len(dict2[word])) )
        tf_idf = TF * IDF
        dict6[URL][word] = tf_idf

#Don't even try adding this dictionary
'''
        page = Page(dict3[URL], URL, dict4[URL], word, tf_idf)
        list = []
        if word not in dict.keys():
            list = [page]
            dict[word] = list
            print page.url
        else:
            dict[word].append(page)
            print page.url
'''

print("done parsing")
#Sends Dictionaries to files

with open('dict1.txt', 'w+') as file:
    json.dump(dict1, file)

with open('dict2.txt', 'w+') as file:
    json.dump(dict2, file)

with open('dict3.txt', 'w+') as file:
    json.dump(dict3, file)

with open('dict4.txt', 'w+') as file:
    json.dump(dict4, file)

with open('dict5.txt', 'w+') as file:
    json.dump(dict5, file)

with open('dict6.txt', 'w+') as file:
    json.dump(dict6, file)

#Our search engine list, sorted by rank with hash for lookup
search = []

#Search Engine
flag = 0
while (flag == 0):
    term = raw_input("Enter in a search term: ").lower()
    if term not in dict2.keys():
        print("Try a better search!\n")
    else:
        for url in dict2[term]:
             page = Page(dict3[url], url, dict4[url], term, dict6[url][term])
             search.append(page)
        search.sort(key=lambda x: x.rank, reverse=True)
        for x in search:
            print (x.url + "\t" + str(x.rank))
        print("\n")
