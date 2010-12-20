import socket
from cPickle import dumps, loads

class player_client():
    def __init__(self, port = 5000):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect_ex(("localhost", port))

    def chat(self):
#        while 1:
        data = loads(self.client_socket.recv(512))
        if (data["quit"]):
            self.client_socket.close()
#            break;
        else:
            print "RECIEVED:" , data
            data = self.display(data)
            if (not data["quit"]):
                self.client_socket.send(dumps(data))
            else:
                self.client_socket.send(dumps(data))
                self.client_socket.close()
#                break;
    def display(self, data):
        data["msg"] = "Whats shaken?"
        #x = raw_input()
        return data


if __name__ == "__main__":
    p = player_client()
    p.chat()


