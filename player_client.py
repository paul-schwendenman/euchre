#/ usr/bin/env python
# filename: tmc.py (CLIENT)

import socket

class player_client():
    def __init__(self, index = 0):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 5000 + index))

    def wait(self):
        s = self.s
        while 1:
            data = s.recv(1000000)
            if not data:
                break
        data = self.do_something(data)
        s.send(data)
    def do_something(self, msg):
        return msg
    def __del__(self):
        self.s.close()
        

p = player_client()
p.wait()


i = 0
while False:
    data = s.recv(1000000)
    i+=1
    if (i<5):
        print data
    if not data:
        break
    print 'received', len(data), 'bytes'
