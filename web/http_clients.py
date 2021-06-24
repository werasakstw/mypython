from urllib import request, parse
import json

parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}
querystring = parse.urlencode(parms)

url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'

def get_post():
    ## GET
    res = request.urlopen(url_get + '?' + querystring).read()

    ## POST
    # res = request.urlopen(url_post, querystring.encode('ascii')).read()
    
    # print(res)            ## bytes str
    # print(res.decode())   ## str
    
    js = json.loads(res)
    print(js)
    # print(js['url'])
    # print(js['form'])
    # print(js['args'])
    # print(js['headers']) 
# get_post()

##-------------------------------------------##

headers = {
    'User-agent' : 'john',
    'Accept-Encoding' : 'identity'
}

def request_with_headers():
    req = request.Request(url_get + '?' + querystring, headers=headers)
    # req = request.Request(url_post, querystring.encode('ascii'), headers=headers)
    res = request.urlopen(req)
    
    for h in res.getheaders():
        print(h)
    # print(res.info())
    # print(res.getheader('Content-Type'))
# request_with_headers()

############################################################

import requests

def requests_test():
    url = url_get + '?' + querystring
    res = requests.get(url, data=parms, headers=headers)
    # res = requests.post(url_post, data=parms, headers=headers)
  
    js = json.loads(res.text)
    print(js)
    # print(js['url'])
# requests_test()

############################################################

from http.client import HTTPConnection
def get_test():
    c = HTTPConnection('www.google.com', 80)
    c.request('GET', '/index.html') 
    res = c.getresponse()
    
    print(res.getcode())
    print(res.getheaders())
    # for l in res.readlines():
    #    print(l)
# get_test()




