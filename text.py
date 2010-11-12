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
