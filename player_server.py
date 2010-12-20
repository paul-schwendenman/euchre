import socket
from cPickle import dumps, loads

def open_socket(port = 5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(5)
    return server_socket

class player_server():
    def __init__(self, server_socket):
        "TCPServer Waiting for client on port XXXX"
        self.client_socket, address = server_socket.accept()
        #print "I got a connection from ", address

    def chat(self, **data):
        try:
            data["quit"]
        except KeyError:
            data["quit"] = 0
        if (data["quit"]):
            self.client_socket.send (dumps(data))
            self.client_socket.close()
        else:
            self.client_socket.send(dumps(data))
 
            data = loads(self.client_socket.recv(512))
            if (data["quit"]):
                self.client_socket.close()
        return data
#    def ask(self, top_card = None, trump = None, played_cards = 0, cards = [], msg = "", error = "", players = 0, dealer = None, team = []):
    ask = chat                
if __name__ == "__main__":
    server_socket = open_socket()
    a = {"quit":0,"msg":"yes"}
    p = player_server(server_socket)
    p2 = player_server(server_socket)
    print "echo 1",p.chat(**a)
    print "echo 2",p2.chat(**a)
    print "echo 1",p.chat(**{"quit":0,"a":0,"gr":54})
    print "echo 2",p2.ask(a=4,gf=5, quit =0)
 
    a["quit"] = 1
    print "close 1",p.chat(**a)
    print "close 2",p2.chat(**a)
