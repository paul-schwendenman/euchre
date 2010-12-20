import player_test
import socket
from cPickle import dumps, loads

class player_client():
    def __init__(self, player, port = 5000):
        self.player = player
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect_ex(("localhost", port))

    def chat(self):
        data = loads(self.client_socket.recv(512))
        if (data["quit"]):
            self.client_socket.close()
        else:
            data = self.ask(data)
            if (not data["quit"]):
                self.client_socket.send(dumps(data))
            else:
                self.client_socket.send(dumps(data))
                self.client_socket.close()
        return data
    def ask(self, data):
        try:
            del data["quit"]
        except KeyError:
            pass
        data["result"] = self.player.ask(**data)        
        if data["result"] == "q" or data["result"] == "Q":
            data["quit"] = 1
        else:
            data["quit"] = 0
        return data


if __name__ == "__main__":
    player = player_test.player_test()
    p = player_client(player)
    data = {}
    data["quit"] = 0
    while not data["quit"]:
        data = p.chat()
        print data


