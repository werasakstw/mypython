# pip install beautifulsoup4

from bs4 import BeautifulSoup
##print( BeautifulSoup('<p>Hello World</p>', features='html.parser') )

import urllib.request
def bs4_test():
    url = urllib.request.urlopen('http://localhost:8080/index.html')
    bso = BeautifulSoup(url, features='html.parser')
##    print(bso)
    print(bso.title)
##    print(bso.body)
##    print(bso.body.h1)
##    print(bso.body.a)
##bs4_test()

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)
def find_test():
    url = urllib.request.urlopen('http://localhost:8080/find.html')
    bso = BeautifulSoup(url, features='html.parser')

    # Find the first span with class.
##    print(bso.find('span', {'class' : 'student'}).get_text())
       
    # Find all span with class.
##    for s in bso.findAll('span', {'class' : 'student'}):
##        print(s.get_text())

    # Find all div with id.
##    for s in bso.findAll('div', {'id' : 'teacher'}):
##        print(s.get_text())
    
    # Find by id.
##    for s in bso.findAll(id='teacher'):
##        print(s.get_text())
        
    # Find more than one tags.
##    for s in bso.findAll({'span', 'div'}):
##        print(s.get_text())
##find_test()

## Table:
def table_test():
    url = urllib.request.urlopen('http://localhost:8080/table.html')
    bso = BeautifulSoup(url, features='html.parser')
    for c in bso.find('table', {'id': 'students'}).children:
        if c != '\n':
            sc = str(c)
            if '<th>' in sc:  ## skip the header
                continue
            print(sc[8:-10].split('</td><td>'))
##table_test()

## Crawling:
def find_links():
    url = urllib.request.urlopen('http://localhost:8080/link.html')
    bso = BeautifulSoup(url, features='html.parser')
    for link in bso.findAll('a'):
        if 'href' in link.attrs: 
            print(link.attrs['href'])
##find_links()

# Crawling an Entire Site
import re
pages = set()
def crawl_wiki(pageUrl):
    global pages
    url = urllib.request.urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(url, features='html.parser')
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                crawl_wiki(newPage)
##crawl_wiki('')
