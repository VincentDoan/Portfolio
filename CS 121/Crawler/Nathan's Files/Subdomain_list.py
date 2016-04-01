'''
 - How many subdomains did you find?
 - Submit the list of subdomains ordered alphabetically
 - and the number of unique pages detected in each subdomain.
 - The file should be called Subdomains.txt,
 - Its content should be lines containing the URL, a comma, a space, and the number.
     of the form: URL, ###
'''
from collections import defaultdict
from urlparse import urlparse

class SubdomainList:
    def __init__(self, inputFileName):
        self.subdomainDict = defaultdict(int)     # Stores Subdomains and the number of pages in each
        self.read_file(inputFileName)             # Read in a list of URL's from a .txt file

    def parseURL(self, url):
        ''' Reads in a url, strips the www. from the front, and returns the subdomain name of ics.uci.edu domain sites
        (removes the .ics.uci.edu) or sorts it into a list of non ICS domain sites.
        :param url:
        '''
        parsed = urlparse(url.replace("www.", "").lower())
        if "ics.uci.edu" in parsed.netloc:
            return parsed.netloc.split("ics.uci.edu")[0]
        else:
            if parsed.netloc.strip() != '':
                return "non ICS domains"

    def read_file(self, inputFileName):
        ''' Reads in an file name string, parses the subdomains from .ics.uci.edu sites, stores them in local
        subdomainDict
        :param inputFileName:
        '''
        with open(inputFileName, 'r') as infile:
            for line in infile:
                url = self.parseURL(line).rstrip(".")
                if url == '':
                    continue
                if self.subdomainDict.has_key(url):
                    self.subdomainDict[url] += 1
                else:
                    self.subdomainDict[url] = 1

    def sendToFile(self):
        ''' Writes the total number of unique subdomains and a list of the alphabetized Subdomain/number of pages value
            pairs seprated by a comma and a space. i.e: subdmain, ###
        '''
        with open("Subdomains.txt", 'w') as outfile:
            outfile.write("{:} {:}\n\n".format("Number of Subdomains:", self.subdomainDict.items().__len__()))
            outfile.write("{:}, {:}\n".format("Subdomain", "Number of pages"))
            for i in sorted(self.subdomainDict.keys()):
                if "non ICS domains" not in i:
                    outfile.write("{:}, {:}\n".format(i, self.subdomainDict[i]))
            if self.subdomainDict.has_key("non ICS domains"):
                outfile.write("\n{:}, {:}\n".format("non ICS domains", self.subdomainDict["non ICS domains"]))

    def printSubdomains(self):
        ''' Displays the total number of unique subdomains and a list, in an easily readable format,
            of the alphabetized Subdomain/number of pages value pairs
        '''
        print "{:<30} {:}\n".format("Number of Subdomains:", self.subdomainDict.items().__len__())
        print "{:<30} {:}".format("Subdomain", "Number of pages")
        for i in sorted(self.subdomainDict.keys()):
            if "non ICS domains" not in i:
                print "{:<30} {:}".format(i, self.subdomainDict[i])
        if self.subdomainDict.has_key("non ICS domains"):
            print "\n{:<30} {:}".format("non ICS domains", self.subdomainDict["non ICS domains"])

if __name__ == "__main__":

    d = SubdomainList("test.txt")
    d.sendToFile()
    #d.printSubdomains()