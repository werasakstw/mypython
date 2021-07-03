import socket

HOST = '127.0.0.1'
PORT = 12345
MAX_BYTES = 1024

def server():           #  Datagram Server
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        name, address = sock.recvfrom(MAX_BYTES)
        name = name.decode()
        print(name)
        sock.sendto(('Hello ' + name).encode(), address)
server()

def client(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(name.encode(), (HOST, PORT))
    data, address = sock.recvfrom(MAX_BYTES)
    print(data.decode())
##client('John')
