import curses
import euchre

A = euchre.card("A","C")
B = euchre.card("9","C")
C = euchre.card("K","H")
D = euchre.card("J","D")

def display(top_card = None, trump = "S", dealer = 0, played_cards = [], cards = None, team = [4,5], msg = "", error = ""):
    ## Pulled from curses.wrapper 2.6, modified.
    try:
        # Initialize curses
        stdscr = curses.initscr()

        # Turn off echoing of keys, and enter cbreak mode,
        # where no buffering is performed on keyboard input
        curses.noecho()
        curses.cbreak()

        # In keypad mode, escape sequences for special keys
        # (like the cursor keys) will be interpreted and
        # a special value like curses.KEY_LEFT will be returned
        stdscr.keypad(1)

        # Start color, too.  Harmless if the terminal doesn't have
        # color; user can test with has_color() later on.  The try/catch
        # works around a minor bit of over-conscientiousness in the curses
        # module -- the error return from C start_color() is ignorable.
        try:
            curses.start_color()
        except:
            pass

        #return func(stdscr, *args, **kwargs)
        return my.table(stdscr, top_card, trump, dealer, played_cards, cards, team, msg, error)
    finally:
        # Set everything back to normal
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()


class table():
    def __init__(self):
#        self.played_cards = [A, D, C, B]
#        self.played_cards = [C, D, A]
        self.played_cards = [A, C]
#        self.played_cards = [A]
#        self.played_cards = []
        self.cards = euchre.hand()
        self.cards.cards = 4 * [A] + [B]
        self.team = [4, 5]
        self.msg = "play these cards? "
    def table(self, scr, top_card, trump, dealer, played_cards, cards, team, msg, error):
        #self.msg = str(curses.has_colors())
        if (len(played_cards) == 0):
            p1 = "1: "
            pa = "P: "
            p3 = "3: "
            u  = "U: "
        elif (len(played_cards) == 1):
            p1 = "1: "
            pa = "P: "
            p3 = "3: " + str(played_cards[0])
            u  = "U: "
        elif (len(played_cards) == 2):
            p1 = "1: "
            pa = "P: " + str(played_cards[0])
            p3 = "3: " + str(played_cards[1])
            u  = "U: "
        elif (len(played_cards) == 3):
            p1 = "1: "
            pa = "P: " + str(played_cards[0])
            p3 = "3: " + str(played_cards[1])
            u  = "U: " + str(played_cards[2])
        elif (len(played_cards) == 4):
            p1 = "1: " + str(played_cards[0])
            pa = "P: " + str(played_cards[1])
            p3 = "3: " + str(played_cards[2])
            u  = "U: " + str(played_cards[3])
    
    
        #player 1
        scr.move(12, 2)
        scr.addstr(p1)
        #partner
        #scr.move(1, 22)
        #scr.addstr("[]")
        scr.move(2, 22)
        scr.addstr(pa)
        
        #player3
        scr.move(12, 44)
        scr.addstr(p3)
        
        #you
        scr.move(22, 22)
        scr.addstr(u)
        
        #points
        scr.move(21,44)
        scr.addstr("Team 1: " + str(team[0]))
        scr.move(22,44)
        scr.addstr("Team 2: " + str(team[1]))
    
        #trump
        scr.move(23,1)
        scr.addstr("Trump: " + str(trump))

        #cards
        scr.move(24, 1)
        scr.addstr("Your cards: " + str(cards))        

        #error msg
        scr.move(23, 15)
        if not (error == ""):
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
            scr.addstr(error, curses.color_pair(1))        


        #msg
        scr.move(25, 1)
        scr.addstr(msg)        
        #input line

        #Refresh
        scr.refresh()
        scr.border()
#        scr.move(12,22) move to center
        #return scr.getch()
        return scr.getkey()

#curses.wrapper(table, [])
#curses.wrapper(table, [], [1, 6])
my = table()
print display(msg = my.msg, played_cards = my.played_cards)
print display(msg = my.msg, played_cards = my.played_cards, error = "Invalid Play!")
