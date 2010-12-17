import socket

class player_client():
    def __init__(self, index = 0):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("localhost", 5000 + index))

    def chat(self):
        while 1:
            data = self.client_socket.recv(512)
            if ( data == 'q' or data == 'Q'):
                self.client_socket.close()
                break;
            else:
                print "RECIEVED:" , data
                data = raw_input ( "SEND( TYPE q or Q to Quit):" )
                if (data <> 'Q' and data <> 'q'):
                    self.client_socket.send(data)
                else:
                    self.client_socket.send(data)
                    self.client_socket.close()
                    break;
                    

if __name__ == "__main__":
    p = player_client()
    p.chat()


