from urllib.request import urlopen

def get_page():
    res = urlopen('http://localhost:8080')     ## http.client.HTTPResponse
    page = res.read()       ## byte array
    txt = page.decode()     ## string
    print(txt)
##get_page()
         
def hello_count():
    txt = urlopen('http://localhost:8080/hello.html').read().decode()
    pattern = '[Hh]ello'    # Regular Expression
    dic = {}
    for w in re.findall(pattern, txt):
        if w in dic:
            dic[w] +=1
        else:
            dic[w] = 1
    print(dic)
##hello_count()

''' HTMLParser:
Parsing an html is the process of finding the start tags, end tags, and data
then process each of them.
'''
from html.parser import HTMLParser
def parse():
    class MyParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print('start:', tag, attrs)
        def handle_endtag(self, tag):
            print('end:', tag)
        def handle_data(self, data):
            print('data:', data)
    
    page = urlopen('http://localhost:8080/hello.html').read().decode()
    MyParser().feed(page)
##parse()

# Ex. Links Collector:
from urllib.parse import urljoin
def link_collector():
    class Collector(HTMLParser):
        def __init__(self, url):
            HTMLParser.__init__(self)
            self.url = url
            self.links = []
        def handle_starttag(self, tag, attrs):
            if tag == 'a' :
                for attr in attrs:
                    if attr[0] == 'href' :
                        absolute = urljoin(self.url, attr[1])
                        if absolute[:4] == 'http' :
                            self.links.append(absolute)
        def get_links(self):
            return self.links

    url = 'http://localhost:8080/link.html'
    c = Collector(url)
    c.feed(urlopen(url).read().decode())
    for l in c.get_links():
        print(l)
##link_collector()

## Regular Expression:
##      .  Matches any (Unicode) character except the new line character ('\n').
##      *  Matches 0 or more repetitions of the previous character.
##      +  Matches 1 or more repetitions of the previous character.
##      ?  Matches 0 or 1 repetition of the previous character.
##      [] Matches any one character listed within.
##      -  used within [], specifies a range of characters(Unicode order).
##      ^  Not match characters in the list or range.
##      |  Or operator, for combining expressions.
##      \d Matches any decimal digit; equivalent to [0-9]
##      \D Matches any nondigit character; equivalent to [^0-9]
##      \s Matches any whitespace character including the blank space,
##          the tab \t, the new line \n, and the carriage return \r
##      \S Matches any non-whitespace character
##      \w Matches any alphanumeric character; this is equivalent to [a-zA-Z0-9_]
##      \W Matches any nonalphanumeric character; this is equivalent to [^a-zA-Z0-9_]
import re
def re_test():
    txt = 'Hello how do you do?'
    print(re.findall('o+\D', txt))

    m = re.search('do', txt)
    print(m.start(), m.end())
# re_test()
