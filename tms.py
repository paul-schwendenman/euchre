#!/ usr/bin/env python
# tms.py (SERVER)
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = int(sys.argv[1])
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print 'client is at', addr
data = conn.recv(1000000)
data = data * 10
z = raw_input()
conn.send(data)
conn.close()
