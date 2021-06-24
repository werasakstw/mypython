from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8000))
s.send(b'Hello')
print(s.recv(8192).decode())
