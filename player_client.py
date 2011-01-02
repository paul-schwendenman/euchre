import socket
from cPickle import dumps, loads
import time

class player_client():
    def __init__(self, player, port = 5000):
        self.player = player
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            for i in range(0,15):
                if not self.client_socket.connect_ex(("sarcasm.ath.cx", port)):
#                if not self.client_socket.connect_ex(("localhost", port)):
                    break
                time.sleep(1)
            self.client_socket.getpeername()
        except KeyboardInterrupt:
            exit()
        except socket.error:
            print "No connection Found."
            exit()
    def chat(self):
        data = p.recv()
        data = p.ask(data)
        p.send(data)
        return data
    def ask(self, data):
        try:
            del data["quit"]
        except KeyError:
            pass
        data["result"] = self.player.ask(**data)        
#        print "result: ", data["result"]
        if data["result"] == "q" or data["result"] == "Q":
            data["quit"] = 1
        else:
            data["quit"] = 0
        return data
    def recv(self):
        data = self.client_socket.recv(4096)
        try: 
            data = loads(data)
        except EOFError:
            print "Connection Closed"
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
        return data
    def send(self, data):
        its = str(type(data))
        if (its == "<type 'dict'>"):
            if (not data["quit"]):
                self.client_socket.send(dumps(data["result"]))
            else:
                self.client_socket.send(dumps(data["result"]))
                self.client_socket.close()
        elif (its == "<type 'str'>") or (its == "<type 'int'>"):
            if (data != "Q"):
                self.client_socket.send(dumps(data))
            else:
                self.client_socket.send(dumps(data))
                self.client_socket.close()
        else:
            print its
            raise
        

if __name__ == "__main__":
    #import player_test
    import player_curses
    #import comp

    player = player_curses.player_curses()
    #player = comp.comp()
    p = player_client(player)
    data = {}
    data["quit"] = 0
    while not data["quit"]:
        data = p.chat()
        print data["result"]
        #data = p.recv()
        #data = p.ask(data)
        #p.send(data)


