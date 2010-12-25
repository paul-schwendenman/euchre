import player_test
import player_curses
import socket
from pickle import dumps, loads
import time

class player_client():
    def __init__(self, player, port = 5000):
        self.player = player
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            for i in range(0,15):
                if not self.client_socket.connect_ex(("localhost", port)):
                    break
                time.sleep(1)
            self.client_socket.getpeername()
        except KeyboardInterrupt:
            exit()
        except socket.error:
            print "No connection Found."
            exit()
    def chat(self):
        data = self.client_socket.recv(4096)
        try: 
            data = loads(data)
        except EOFError:
            print "something is wrong"
            data = {"quit":1}
        except:
            import sys
            print "Unexpected error:", sys.exc_info()[0]
            raise

#        for card in data["cards"]:
#            print card,
#        print
        if (data["quit"]):
            self.client_socket.close()
        else:
            data = self.ask(data)
            if (not data["quit"]):
                self.client_socket.send(dumps(data["result"]))
            else:
                self.client_socket.send(dumps(data["result"]))
                self.client_socket.close()
        return data
    def ask(self, data):
        try:
            del data["quit"]
        except KeyError:
            pass
        data["result"] = self.player.ask(**data)        
        print "result: ", data["result"]
        if data["result"] == "q" or data["result"] == "Q":
            data["quit"] = 1
        else:
            data["quit"] = 0
        return data
    def recv():
        data = self.client_socket.recv(1024)
        #print data
        try:
            data = loads(da)
        except:
            pass
        return data


if __name__ == "__main__":
    player = player_curses.player_curses()
    p = player_client(player)
    data = {}
    data["quit"] = 0
    while not data["quit"]:
        data = p.chat()


