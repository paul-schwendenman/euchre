import socket
import sys

port = 5643

class player_server():
    def __init__(self):
        import socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("", 5000))
        self.server_socket.listen(5)

    def chat(self):
        print "TCPServer Waiting for client on port 5000"
        while 1:
                client_socket, address = self.server_socket.accept()
                print "I got a connection from ", address
                while 1:
                        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
                        if (data == 'Q' or data == 'q'):
                                client_socket.send (data)
                                client_socket.close()
                                break;
                        else:
                                client_socket.send(data)
         
                        data = client_socket.recv(512)
                        if ( data == 'q' or data == 'Q'):
                                client_socket.close()
                                break;
                        else:
                                print "RECIEVED:" , data
                
if __name__ == "__main__":
    p = player_server()
    p.chat()
 