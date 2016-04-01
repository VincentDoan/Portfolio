import json
import os
import sys

class Page:
    def __init__(self,url,txt):
        self.url = url
        self.txt = txt

def load():
    path = r'C:\Users\Buddy\PycharmProjects\CS121Indexer'

    with open(os.path.join(path, 'dict2.txt'),'r') as data_file:
        dict2 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict3.txt'),'r') as data_file:
        dict3 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict4.txt'),'r') as data_file:
        dict4 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict5.txt'),'r') as data_file:
        dict5 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict6.txt'),'r') as data_file:
        dict6 = json.loads(data_file.read())

def search(terms, dict2, dict3, dict4, dict5, dict6):
    path = r'C:\Users\Buddy\PycharmProjects\CS121Indexer\file\FileDump'

    dict7 = {}
    input = []
    list = []
    ordered_List = []

    for word in terms.split():
        if word != word.upper():
            word = word.lower()
        input.append(word)

    #This part scores URLs based on TF-IDF
    for word in input:
        try:
            for url in dict2[word]:
                try:
                    dict7[url] += dict6[url][word] #* dict5[url]
                except:
                    dict7[url] = dict6[url][word] #* dict5[url]
            for url in dict7:
                if word not in dict6[url]:
                    dict7[url] *= .1
        except:
            pass


    #This part Scores URLs based on appearence of keyterms in the title
    count = 1
    for url in dict7:
        for word in input:
            if word not in dict4[url]:
                count *= .5
        dict7[url] = (dict7[url] * .25) + (count * .75)
        count = 1

    list = sorted(dict7, key=dict7.get, reverse=True)

    if(len(list) <5):
        length = len(list)
    else:
        length = 5
    for i in range(0,length):
        try:
            #get json file of url
            txt = ''
            file_name = str(dict3[list[i]]) + '.txt'
            data_file = open(os.path.join(path, file_name),'r')
            file = json.loads(data_file.read())

            #save body of text in a list
            text = []
            for word in file['text'].split():
                text.append(word)

            #save URl and 1st instance of term + next 15 words in page object
            j = 0
            for word in text:
                if word in input:
                    try:
                        track = j
                        while track < j+15:
                            txt += text[track] + " "
                            track += 1
                        break
                    except:
                        pass
                j += 1
        except IndexError:
            pass
        ordered_List.append(Page(list[i], txt))
    return ordered_List

if __name__ == "__main__":
    path = r'C:\Users\Buddy\PycharmProjects\CS121Indexer'

    with open(os.path.join(path, 'dict2.txt'),'r') as data_file:
        dict2 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict3.txt'),'r') as data_file:
        dict3 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict4.txt'),'r') as data_file:
        dict4 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict5.txt'),'r') as data_file:
        dict5 = json.loads(data_file.read())

    with open(os.path.join(path, 'dict6.txt'),'r') as data_file:
        dict6 = json.loads(data_file.read())

    print('searching')



    for i in search("mondego", dict2, dict3, dict4, dict5, dict6):
        print(i.url)
        print(i.txt)