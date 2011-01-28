import socket
from multiprocessing import Pool

port = 5000


# A revised version of our thread class:
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

    #Create our pool:
    p = Pool(1)
    print p
    ports = [port + i for i in range(1, 16)]
    ports.reverse()
    print ports
     
    # Set up the server:
    server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    server.bind ( ( '', port ) )
    server.listen ( 5 )

    # Have the server serve "forever":
    client, address = server.accept()

    print 'Received connection:', client 
    #Spawn a process and send the information
    print ports
    port = ports.pop()
    print "mapping", port
    p.apply_async(f, [port])
    client.send (str(port))
    client.close()

    print 'Closed connection:', client 

    import time
    time.sleep(10)
    p.close()
    p.terminate()    
    p.join()
    
            