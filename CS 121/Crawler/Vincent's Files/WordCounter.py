__author__ = 'Ryan'

#http://stackoverflow.com/questions/2988211/how-to-read-a-single-character-at-a-time-from-a-file-in-python
# I got help from reading from a file character by character from that link ^
#f = open('text.txt', 'r')


string = ""
words = []
hash = {}
freq = []
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
with open("text.txt") as f:
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
      print "End of file"
      break

#checks if words are in stopword hash, adds if it isn't. DOES NOT ADD random apostrophes and hyphens
if (words.__sizeof__() >  0):
    for item in words:
       if (item == "'" or item == "-" or item.isdigit() or item.__len__() < 3):
           pass
       else:
        if not (item in hash):
              hash[item] = 1
        else:
              hash[item] = hash[item] + 1
#print hash

#sort the keys to hash and then adds to freq list. freq list is then sorted by frequencies
for i in sorted(hash.keys()):
    freq.append((i, hash[i]))

freq.sort(key=lambda x: x[1], reverse=True)


#prints the 500 most frequent words into CommonWords.txt
x = 0
f = open('CommonWords.txt', 'w')
print freq.__len__()
if(freq.__len__() > 499):
    for x in range(0, 500):
        string = str(freq[x])
        f.write(string + "\n")
else:
    for i in freq:
        f.write(str(i))
        f.write("\n")

f.close()

#print(freq)

#for word in words:
   # print word
#print(words)
#sorted(words)
#print(words)
#for word in words:
 #   print word

#parsed word class
#class parsedWord:
 #   string = ""
 #   count = 0
 #   def __init__(self, string, count):
  #      self.string = string
  #      self.count = count

   # f.write('\n'.join('%s %s' % x for x in freq))
  #  f.write("\n")

  #freq.sort(reverse = True)
#print freq
    #print (i + str(hash[i]))
#hash["YO BRO"] = 0

#print hash.__contains__(0)
#print hash.get(0)
#print "YO BRO" in hash
#for item in words:
      #  print item
#wurd = parsedWord("YO BRO", 1)

#print(wurd.string)
#print(wurd.count)
#print(words)
#frequency = 0
#name = "zzzzzzzzzzzzzzzzzzzzz"

#while (hash):
 #   for i in hash.keys():
      #  print(hash[i])
       # print(i)
       # if (hash[i] > frequency and i < name):
        #    name = hash.get(i)
         #   frequency = hash[i]
    #freq.append((name, frequency))
    #del hash[name]