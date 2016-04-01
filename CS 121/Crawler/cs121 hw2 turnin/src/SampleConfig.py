#Theodore Matula Jr. tmatulaj
#Vincent Doan  vhdoan
#Nathanial Alan Benjamin nbenjami
import re

try:
    # For python 2
    from urlparse import urlparse, parse_qs
except ImportError:
    # For python 3
    from urllib.parse import urlparse, parse_qs

from Crawler4py.Config import Config

class SampleConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.PolitenessDelay = 1000
        #self.MaxDepth = 4
        self.UserAgentString = "UCI Inf141-CS121 crawler 14971857 90117275 67995387"

    def GetSeeds(self):
        '''Returns the first set of urls to start crawling from'''
        return ["http://www.ics.uci.edu/"]

    def HandleData(self, parsedData):
        '''Function to handle url data. Guaranteed to be Thread safe.
        parsedData = {"url" : "url", "text" : "text data from html", "html" : "raw html data"}
        Advisable to make this function light. Data can be massaged later. Storing data probably is more important'''
        print("url = " + parsedData["url"])
        
        #prints current URL to file
        f = open('test.txt', 'a')
        f.write(parsedData["url"].encode('utf-8') + "\n")
        f.close()

        with open('text.txt', 'a') as textFile:
            textFile.write(parsedData["text"].encode('utf-8') + "\n")
            
        #finds and keeps track of URL with longest text. The first line has the length of 
        #URL with the longest text, in words.
        #note that if longestText.txt already has text in it when the crawler starts,
        #a '0' will be added to the end of the URL on the next line, so be careful of that. Might fix that later
        
        #Only works if parsedData["text"] is a string with propor spaces, which i still need to try out.
        #Works on regular string with spaces though.
        currentTextLength = len(parsedData["text"].split())
        longestText = open('longestText.txt', 'r+')
        highestCount = longestText.readline()
            
        if currentTextLength > int(highestCount):
            longestText.seek(0)
            longestText.truncate()
                
            longestText.write('{}'.format(currentTextLength) + "\n" + '{}'.format(parsedData["url"]))
            
        longestText.close()
        return

    def ValidUrl(self, url):
        '''Function to determine if the url is a valid url that should be fetched or not.'''
        parsed = urlparse(url)
        try:
            if "duttgroup" in parsed.hostname or "vision" in parsed.hostname or "cml" in parsed.hostname \
                    or "mailman" in parsed.hostname or "calendar" in parsed.hostname or "evoke" in parsed.hostname \
                    or "gonet.genomics" in url or "sli.ics.uci.edu/Classes" in url or "timesheet.ics.uci.edu" in parsed.hostname \
                    or "survey-web.ics.uci.edu" in parsed.hostname or "intranet.ics.uci.edu" in parsed.hostname or "fano.ics.uci.edu" in parsed.hostname or "archive.ics.uci.edu" in parsed.hostname:
                    return False
            return ".ics.uci.edu" in parsed.hostname \
                and not re.match(".*\.(css|js|bmp|gif|jpe?g|jpg|jpeg|ico|GIF|gif" + "|png|tiff?|mid|mp2|mp3|mp4"\
			    + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
			    + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
			    + "|thmx|mso|arff|rtf|jar|csv"\
			    + "|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path)
        except TypeError:
            print ("TypeError for ", parsed)