 Enter your code here. Read input from STDIN. Print output to STDOUT
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
       
        if "\n" in data :
            print ">>> Multi-line Comment"
            
        else:
            print ">>> Single-line Comment"
        print data
            
    def handle_data(self, data):
        if data=="\n": return
        print ">>> Data"
        print data


N = int(input())
htmlParser = MyHTMLParser()
html = ""

for _ in range(N):
    html += raw_input().strip()+"\n"

htmlParser.feed(html)    


