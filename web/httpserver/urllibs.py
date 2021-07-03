
from urllib import request   
def urllib_test():
    url = 'http://127.0.0.1:8080'
    res = request.urlopen(url)     # HTTPResponse object
    print(res.url)
    print(res.status)

##    print(res.getheader('Content-Type'))
##    for i in res.getheaders():
##        print(i)
        
##    print(res.read())               # byte str
##urllib_test()

def request_test():
    req = request.Request('http://127.0.0.1:8080')
    print(req.full_url)
    print(req.get_method())
    print(req.data)
    print(req.header_items())
    
    req.add_header('Accept-Language', 'th')
    print(req.header_items())
##request_test()

# Params encode.
parms = {               # Python dict
    'id': 123,
    'name': 'John Rambo'
}
from urllib import parse
querystring = parse.urlencode(parms)
##print(querystring)      # id=123&name=John+Rambo

# Request with header
headers = {
    'User-agent' : 'john',
    'Accept-Encoding' : 'utf8'
}
def request_header():
    req = request.Request(url1 + '?' + querystring, headers=headers)   
    res = request.urlopen(req)
    for h in res.getheaders():
        print(h)
##request_header()

def response_test():
    url = 'http://127.0.0.1:8080'
    res = urllib.request.urlopen(url)
    print(res)
    print(res.url)
    print(res.readline())
    print(res.read(7))
    print(res.read())
    print()
    print(urllib.request.urlopen(url).read().decode())
# response_test()

#-----------------------------------------------------------------

## Encoding defines content compression.
## Check if the server support an encoding.
##  gzip, compress, deflate, and identity.
def encoding_check():
    req = request.Request('http://www.google.com')
##    req = request.Request('http://www.yahoo.com')
##    req = request.Request('http://127.0.0.1:8080')
    
    req.add_header('Accept-Encoding', 'gzip')
##    req.add_header('Accept-Encoding', 'identity')
##    req.add_header('Accept-Encoding', 'deflate, gzip, compress')
    
    res = request.urlopen(req)
    print(res.getheader('Content-Encoding'))
##encoding_check()

import gzip
def gzip_test():
    req = request.Request('http://www.google.com')
    req.add_header('Accept-Encoding', 'gzip')
    # req.add_header('Accept-Encoding', 'identity')
    
    content = request.urlopen(req).read()
    content = gzip.decompress(content)
    for l in content.splitlines()[:5]:
        print(l)
##gzip_test()
