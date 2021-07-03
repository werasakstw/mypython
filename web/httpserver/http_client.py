import socket
HOST = '127.0.0.1'
PORT = 8080
def socket_client():
    req = ('GET / HTTP/1.1\r\n'
           'Host: {host}:{port}\r\n\r\n').format(
                host = HOST,
                port = PORT)
    with socket.create_connection((HOST, PORT)) as sk:
        sk.sendall(req.encode())
        ba = bytearray()
        while True:
            b = sk.recv(1024)
            if not len(b):
                break
            ba += b
        print(ba.decode())
##socket_client()

#----------------------------------------------------------

from urllib import request   
def urllib_client():
    url = 'http://127.0.0.1:8080'
    print(request.urlopen(url).read().decode())
# urllib_client()

#-------------------------------------------------------------

import requests
def requests_client():
    url = 'http://127.0.0.1:8080'
    print(requests.get(url).content.decode())
##requests_client()

import io
def clone(site):
    web = requests.get(site).text.encode()
    with io.FileIO('root.html', 'w') as f:
        f.write(web)
##clone('http://localhost:8080')

#-----------------------------------------------------

from http.client import HTTPConnection
def hc_test():
    c = HTTPConnection('127.0.0.1', 8080)
    c.request('GET', '/index.html') 
    res = c.getresponse()
    print(res.getcode())
    for l in res.readlines():
        print(l.decode(), end='')
hc_test()
