import socket
from cPickle import dumps, loads

port = 5643

class player_server():
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("", 5000))
        self.server_socket.listen(5)

    def chat(self, data):
        print "TCPServer Waiting for client on port 5000"
#        while 1:
        client_socket, address = self.server_socket.accept()
        print "I got a connection from ", address
#        while 1:
#        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
        if (data["quit"]):
            client_socket.send (dumps(data))
            client_socket.close()
#            break;
        else:
            client_socket.send(dumps(data))
 
            data = loads(client_socket.recv(512))
            if ( data == 'q' or data == 'Q'):
                client_socket.close()
#                break;
            else:
                print "RECIEVED:" , data
        return data                                
                
if __name__ == "__main__":
    a = {"quit":0,"msg":"yes"}
    p = player_server()
    #x = raw_input(":")
    print p.chat(a)
#    x = raw_input(":")
#    a["quit"] = 1
#    p.chat(a)
 