import curses

myscreen = curses.initscr()

myscreen.border(0)
myscreen.addstr(12, 25, "Python curses in action!")
myscreen.refresh()

a = myscreen.getch()
#myscreen.flash()
myscreen.addstr(2,2, a)

myscreen.getch()


curses.endwin()



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

