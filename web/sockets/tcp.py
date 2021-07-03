import threading, socket

MAX_BYTES = 1024
HOST = '127.0.0.1'
PORT = 12345

def handler(csk):
    name = csk.recv(1024).decode()
    print(name)
    csk.send(('Hello %s!' % name).encode())
    csk.close()
    
def server1(): 
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((HOST, PORT))
    sk.listen(5)                ## max connection = 5
    print('Listening at {}'.format(sk.getsockname()))
    while True:
        conn, addr = sk.accept()
        print('Connection from: %s: %d' % (addr[0], addr[1]))
        threading.Thread(target=handler, args=(conn,)).start()
##server1()

def server2(): 
    with socket.create_server((HOST, PORT)) as sk:
        print('Listening at {}'.format(sk.getsockname()))
        while True:
            conn, addr = sk.accept()
            print('Connection from: %s: %d' % (addr[0], addr[1]))
            threading.Thread(target=handler, args=(conn,)).start()
##server2()

def client():
    # sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    # sk.connect((HOST, PORT))
    
    sk = socket.create_connection((HOST, PORT))   
    sk.send('John'.encode())
    print(sk.recv(1024).decode())
##client()

