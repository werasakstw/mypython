import socket

HOST = '127.0.0.1'
PORT = 12345
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on', (HOST, PORT))
    while True:
        conn, addr = s.accept()
        with conn:
            name = conn.recv(1024).decode()
            if name == 'bye':
                print('Server shutdown.')
                break
            print('Connected from:', addr, name)
            res = 'Hello ' + name
            conn.send(res.encode())

            
# netstat -an
