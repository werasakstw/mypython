from socket import *

host = '127.0.0.1'
start = 8075
stop = 8085

for p in range(start, stop):
	print('Test port: ' + str(p))
	s = socket(AF_INET, SOCK_STREAM)
	s.settimeout(2)
	if s.connect_ex((host, p)) == 0:
		print(p)
	s.close()
