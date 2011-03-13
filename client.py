#!/usr/bin/python

def run():
    print "Pick a client to run:\n\t1. Tk Client\n\t2. Curses Client\n\t3. Text based Client"
    output = (raw_input('>') + " ").upper()[0]
    if output == '1':
        import player.tk as tk
        tk.run()
    elif output == '2':
        import player.client as client
        client.run_curses()
    elif output == '3':
        import player.client as client
        client.run()
    else:
        print "Recieved invalid option ", output
        print "Quitting"

if __name__ == '__main__':
    run()
