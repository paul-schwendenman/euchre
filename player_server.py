import socket
from cPickle import dumps, loads

port = 5643

def open_socket(port = 5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(5)
    return server_socket

class player_server():
    def __init__(self, server_socket):
        print "TCPServer Waiting for client on port 5000"
#        while 1:
        self.client_socket, address = server_socket.accept()
        print "I got a connection from ", address

    def chat(self, data):
#        while 1:
#        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
        if (data["quit"]):
            self.client_socket.send (dumps(data))
            self.client_socket.close()
#            break;
        else:
            self.client_socket.send(dumps(data))
 
            data = loads(self.client_socket.recv(512))
            if (data["quit"]):
                self.client_socket.close()
#                break;
            else:
                print "RECIEVED:" , data
        return data                                
                
if __name__ == "__main__":
    server_socket = open_socket()
    a = {"quit":0,"msg":"yes"}
    p = player_server(server_socket)
    p2 = player_server(server_socket)
    #x = raw_input(":")
    print p.chat(a)
    print p2.chat(a)
    
#    x = raw_input(":")
    print a
    a["quit"] = 1
    print a
    p.chat(a)
