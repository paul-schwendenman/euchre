import curses

#shuffle
#set scores to zero
##deal cards
##bidding
##lead
##follow suit
##else 
###trump
###throw off



        


class table:
    """Class for the table, has players.
    Needs to handle: leader, dealer, points etc."""
    def __init__(self):
        pass

    def start(self, game):
        """begins a game by adding players"""
        self.game = game
        num_players = 0
        self.players = []
        self.players = [player(), comp(), comp(), comp(), ] 
#        self.players = [testPlayer(), comp(), comp(), comp(), ] 
#        self.players = [player(), player(), player(), player(), ] 
#        self.players = [player(), comp(), player(), comp(), ] 
#        self.players = [comp(), comp(), comp(), comp(), ] 
        for each_player in self.players:
            each_player.set_table(self)
            each_player.tricks_taken = 0
        self.players[0].name = "Paul"
        self.players[1].name = "Phil"
        self.players[2].name = "Sierra"
        self.players[3].name = "Julia"
    def __str__():
        pass
    def _shift(self, n, destructive = 0):
        n = n % len(self.players)
        tail = self.players[n:]
        self.players[n:] = []
        tail.extend(self.players)
        if destructive:
            self.players = tail
        else:
            return tail
        
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
    
class game:
    """Class for each hand in a game, meaning all the stuff needed to play for one hand."""
    def __init__(self):
        pass


    def start(self, table):
        """Starts up the deck and deals"""
        self.table = table
        bid = ""
        dealer = random.randrange(0,4)
        self.table._shift(self.dealer, 1)
        players = table.players
        self.deck = deck()
        self.deck.populate()
        self.deck.cards = self.deck.bubble_sort()
        self.deck.shuffle()
        self.deck.deal(players, self.dealer)

        for each_player in players:
            each_player.index = players.index(each_player)
            each_player.cards = each_player.bubble_sort()

    def bid(self, players):
        """Handles bidding for all players"""
        top_card = self.deck.cards[0]
        bid, index = self.get_bid(players, top_card)
        return (bid, index)
    def play(self, players, bid = 'S'):
        """Handles the card play given a bid"""
        team = 0
        trump = bid
        del bid
        #print "trump:\t\t", trump, "\ndealer:\t\t", self.dealer
        for each_player in players:
            each_player.cards = each_player.bubble_sort(trump)
        leader = self.dealer + 1
#        del self.dealer
        tricks = 5 * [trick()] #tricks = [trick(), trick(), trick(), trick(), trick(),]
        for _trick in tricks:
            #for index, player in enumurate(players):
            for index in range(0, 4):
                #print index
                play_this_card = players[((leader + index) % 4)].get_play(trump, _trick)
                players[((leader + index) % 4)].give(play_this_card, _trick)
                #print "this ", play_this_card
            #print
            winner = _trick.best_card(trump)
            players[winner.owner].tricks_taken += 1 
            #This is a print statement used for debugging
            for _player in players:
                _player.results(winner, leader, _trick)
            
            leader = winner.owner
            if (leader % 2):
                team -= 1
            else:
                team += 1
            
#        for _trick in tricks:
            while (len(_trick.cards) > 0):      
                _trick.give(_trick.cards[0], self.deck)
        return team

    def get_bid(self, players, top_card):
        """Handles the bid recovery for all players"""
        for index in range(1, 5):
            bid = players[((self.dealer + index) % 4)].bid(top_card, self.dealer)
            if self.good_bid(bid):
                players[self.dealer].pick_it_up(top_card)
                return (bid, index)
        for index in range(1, 5):
            bid = players[((self.dealer + index) % 4)].bid()
            if self.good_bid(bid):
                return (bid, index)
        return (bid, index)

    def good_bid(self, bid):
        """tests to see if the bid is "Good" """
        if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
            return 1
        else:
            return 0



class euchre:
    """Highest level class creates a game for play"""
    def __init__(self):
        """Sets up and starts a game."""
        self.table = table()
        
        index = 0
        self.game = game()
        self.game.team = [0, 0]
        team = self.game.team
        self.game.dealer = 0
        while(team[0] < 10 and team[1] < 10):
            self.table.start(self.game)
            self.game.start(self.table)
            (mybid, index) = self.game.bid(self.table.players)
            if (mybid == "P"):
                continue
            print "mybid, index", mybid, index
            result = self.game.play(self.table.players, mybid)            
            #result = self.bid.play(self.table.players)
            if (result == 5):
                team[(index + 1) % 2] += 2
                print "Team %c gains 2" % (['A', 'B'][index % 2])
            elif (result > 0):
                team[(index + 1) % 2] +=1
                print "Team %c gains 1" % (['A', 'B'][index % 2])
            elif (result < 0):
                team[(index + 0) % 2] +=2
                print "Team %c euchred. Team %c gains 2" % ((['A', 'B'][(index) % 2]),(['A', 'B'][(index + 1) % 2]))
            else:
                raise IndexError
            self.table._shift(1)
            self.game.dealer += 1
            self.game.dealer %= 4
        if (team[0] > 10):
            print "Team A wins!... 0, 2"
        else:
            print "Team A wins!... 1, 3"

                
                 

def main():
    euchre()

if __name__ == "__main__":
    main()

