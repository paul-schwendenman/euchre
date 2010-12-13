import "player"

class player_curses(player):
    """Player is inherited from player, is interactive. Has set_hand, get_play, get_bid, pick_it_up, worst_card and highest_nontrump"""
    def display(self, top_card = None, trump = None, played_cards = [], cards = [], msg = "", error = "", players = 0):
        ## Pulled from curses.wrapper 2.6, modified.
        def printCard(card):
            if card == None:
                pass
            elif (card.suit in ["D", "H"]):
                stdscr.addstr(str(card) + ", ", curses.color_pair(2))
            elif (card.suit in ["S", "C"]):
                stdscr.addstr(str(card) + ", ", curses.color_pair(3))
            else:
                stdscr.addstr(str(card) + ", ")
                raise Exception("Suit not H, D, S, C")
            
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
            stdscr.erase()

            if ((25, 50) > stdscr.getmaxyx()):
                raise Exception("Make your window bigger")                 
            #Set Red, Black Cards:
            curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)


            #self.msg = str(curses.has_colors())
            if (len(played_cards) == 0):
                p1 = None
                pa = None
                p3 = None
                u  = None
            elif (len(played_cards) == 1):
                p1 = None
                pa = None
                p3 = played_cards[0]
                u  = None
            elif (len(played_cards) == 2):
                p1 = None
                pa = played_cards[0]
                p3 = played_cards[1]
                u  = None
            elif (len(played_cards) == 3):
                p1 = played_cards[0]
                pa = played_cards[1]
                p3 = played_cards[2]
                u  = None
            elif (len(played_cards) == 4):
                p1 = played_cards[0]
                pa = played_cards[1]
                p3 = played_cards[2]
                u  = played_cards[3]
        
        
            #player 1
            stdscr.move(12, 2)
            if self.game.dealer == 1:
                stdscr.addstr("*1*: ")
            else:    
                stdscr.addstr("1: ")
            printCard(p1)
            stdscr.move(13, 2)
            for i in range(0, self.players[1].tricks_taken):
                stdscr.addstr("[],")
            #partner
            #stdscr.move(1, 22)
            #stdscr.addstr("[]")
            stdscr.move(2, 22)
            if self.game.dealer == 2:
                stdscr.addstr("*P*: ")
            else:    
                stdscr.addstr("P: ")
            printCard(pa)
            stdscr.move(3, 22)
            for i in range(0, self.players[2].tricks_taken):
                stdscr.addstr("[],")
        
            #player3
            stdscr.move(12, 44)
            if self.game.dealer == 3:
                stdscr.addstr("*3*: ")
            else:    
                stdscr.addstr("3: ")

            printCard(p3)
            stdscr.move(13, 44)
            for i in range(0, self.players[3].tricks_taken):
                stdscr.addstr("[],")
            
            #you
            stdscr.move(22, 22)
            if self.game.dealer == 0:
                stdscr.addstr("*U*: ")
            else:    
                stdscr.addstr("U: ")
            printCard(u)

            stdscr.move(23, 22)
            for i in range(0, self.players[0].tricks_taken):
                stdscr.addstr("[],")

            #points
            stdscr.move(21,40)
            stdscr.addstr(" Your Team: " + str(self.game.team[1]))
            stdscr.move(22,40)
            stdscr.addstr("Other Team: " + str(self.game.team[0]))
        
            #trump or top_card - not both
            stdscr.move(23,1)
            if trump:
                stdscr.addstr("Trump: " + str(trump))
            elif top_card:
                stdscr.addstr("Top Card: ")
                printCard(top_card)
    
            #cards
            stdscr.move(24, 1)
            if cards:
                stdscr.addstr("Your cards: ")
                curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
                curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

                for index, card in enumerate(cards):
                    stdscr.addstr(str(index + 1) + ".")
                    printCard(card)
            else:
                stdscr.addstr(msg)        
                msg = ""
    
            #error msg
            stdscr.move(23, 25)
            if not (error == ""):
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                stdscr.addstr(error, curses.color_pair(1))        
    
    
            #msg
            stdscr.move(25, 1)
            stdscr.addstr(msg)        
            #input line
    
            #print each player's hand
            if (players and ((29, 1) < stdscr.getmaxyx())):
                y, x = stdscr.getyx()
                for index, eachPlayer in enumerate(self.players):
                    stdscr.move(y + 1 + index, 1)
                    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
                    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

                    for card in eachPlayer.cards:
                        printCard(card)
                stdscr.move(25, x)                   
    
            #Refresh
            stdscr.refresh()
            stdscr.border()
    #        stdscr.move(12,22) move to center
            #return stdscr.getch()
            return stdscr.getkey()
        finally:
            # Set everything back to normal
            stdscr.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()


