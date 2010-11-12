import curses

def this(myscreen):
  #myscreen = curses.initscr()
  curses.echo()
  myscreen.border(0)
  myscreen.addstr(12, 25, "Python curses in action!")
  myscreen.refresh()
  a = myscreen.getkey()
  myscreen.addstr(2,2, a)

  a = myscreen.getch()
#  b = "This " + a
  curses.flash()
  myscreen.addstr(2,2, str(a))
  
  b = myscreen.getstr()
  myscreen.addstr(2,2, b)

  myscreen.getch()
  curses.endwin()
def table(scr, played_cards):

    if (len(played_cards) == 0):
        p1 = None
        pa = None
        p3 = None
        u  = None

    #player 1
    scr.move(12, 2)
    scr.addstr("*1:")
    #partner
    scr.move(1, 22)
    scr.addstr("[]")
    scr.move(2, 22)
    scr.addstr("P: A of S")
    
    #player3
    scr.move(12, 44)
    scr.addstr("3: 9 of S")
    
    #you
    scr.move(22, 22)
    scr.addstr("U")
    
    #mesg
    scr.move(23, 1)
    
    
    #input line

    #Refresh
    scr.refresh()
    scr.border()
#    scr.move(12,22) move to center
    scr.getch()

curses.wrapper(table, [])
