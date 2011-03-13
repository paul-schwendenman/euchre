#!/usr/bin/python

import Queue
import socket
import threading
from multiprocessing import Pool

port = 5000


# A revised version of our thread class:
class ClientThread ( threading.Thread ):

    # Note that we do not override Thread's __init__ method.
    # The Queue module makes this not necessary.
    def run ( self ):
  
    # Have our thread serve "forever":
        while True:
  
            # Get a client out of the queue
            client = clientPool.get()
            print client
            # Check if we actually have an actual client in the client variable:
            if client != None:
            
                print 'Received connection:', client [ 1 ] [ 0 ]
                #Spawn a process and send the information
                print ports
                port = ports.pop()
                print "mapping", port
                p.apply_async(f, [port])
                client [ 0 ].send (str(port))
                client [ 0 ].close()
            
                print 'Closed connection:', client [ 1 ] [ 0 ]
def f(port):
    import euchre
    print "making euchre"
    euchre.main(port)
    print "euchre done push port"
    ports.push(port)
    print ports

if __name__ == '__main__':
    """Testing"""
#    server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
#    server.bind ( ( '', port ) )
#    server.listen ( 5 )
#    client, address = server.accept()
#    client.send('5001')
#    client.close()
#    f(5001)

    # Create our Queue:
    clientPool = Queue.Queue ( 0 )
    
    #Create our pool:
    p = Pool(5)
    print p
    ports = [port + i for i in range(1, 16)]
    ports.reverse()
    print ports
     
    print "threads running"           
    # Start two threads:
    for x in xrange ( 2 ):
        ClientThread().start()
    
        # Set up the server:
        server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        server.bind ( ( '', port ) )
        server.listen ( 5 )
    
    # Have the server serve "forever":
    while True:
        try:
            clientPool.put ( server.accept() )
        except KeyboardInterrupt:
            break
    try:
        p.close()
    except:
        p.terminate()    
    p.join()
    
            