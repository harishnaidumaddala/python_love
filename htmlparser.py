
from HTMLParser import HTMLParser

class CustomHTMLParser(HTMLParser):

    def _attr_printer(self, attrs):
        if attrs:
            for attr in attrs:
                print "-> " + attr[0] + " > " + str(attr[1]) 

    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        self._attr_printer(attrs)

    def handle_endtag(self, tag):
        print "End   :", tag

    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        self._attr_printer(attrs)

if __name__ == "__main__":

    N = int(input())
    htmlParser = CustomHTMLParser()
    html = ""

    for _ in range(N):
        html += raw_input().strip()

    htmlParser.feed(html)    

