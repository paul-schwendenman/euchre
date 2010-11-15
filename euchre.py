import random
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



# Constants for the euchre game.
ranks = [None, "9", "10", "J", "Q", "K", "A",]
cardname = [None, "9", "10", "J", "Q", "K", "A", "9T", "10T", "QT", "KT", "AT", "LB", "JT"]
cardvalu = [  -1,  1 ,   2 ,  3 ,  4 ,  5 ,  10,  12 ,   15 ,  20 ,  25 ,  30 ,  31 ,  35 ]
values = dict(zip(cardname, cardvalu))
left = { "S" : "C", "C" : "S", "D" : "H", "H" : "D"}
suits = [None, "S", "D", "C", "H"]
suit_chars = [None, unichr(9824), unichr(9827), unichr(9829), unichr(9830)]
#suit_chars = [None, 9824, 9827, 9829, 9830]


class card:
    """Cards are used by the players to organize the game play."""
    def __init__(self, rank = None, suit = None):
        """Makes a new card. by default the card is blank or has no suit or value (rank)."""
        self.rank = rank
        self.suit = suit
        self.ranks = ranks
        self.suits = suits
    def value(self, trump, lead = None):
        """Calculates the value of the card bassed on trump and a lead?
        better was to do this?"""
        value = values[self.relative_suit(trump)]

        #This print statement can be used for debugging
        #print "rank: %2i card: %s trump %s" % (value, self, trump)

        return value
    def relative_suit(self, trump):
        if (self.suit == trump):
            value = self.rank + "T"
        elif (self.rank == "J" and trump == left[self.suit]):
            value = "LB"
        else:
            value = self.rank
        return value
    
    def is_trump(self, trump):
        return (self.relative_suit(trump)).endswith("T")
                
    def __str__(self):
        """prints information of the card in the form: R of S, where R is rank and S is suit"""
#        output = ""
#            output += "%2s of %s" % (self.ranks[self.rank], self.suits[self.suit])
#        if (self.suit == "d" or self.suit == "D" or self.suit == "h" or self.suit == "H"):
#            output += "\033[0;31m"
#        output += "%2s of %s" % (self.rank, self.suit) 
#        output += "\033[m"
#        output += "%2s of" % (self.rank) + suit_chars[suits.index(self.suit)] + "\033[m"
#        return output
        return "%2s of %s" % (self.rank, self.suit)


class hand():
    """Hand is used as the base class for all the rest of the card handlers. Hand of playing cards, base class __init__, __str__, clear, add, remove, and give"""
    def __init__(self):
        """Blank hand. No Cards yet."""
        self.index = 0
        self.cards = []
        self.name = ""
    def __str__(self):
        """Prints a list of cards."""
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + ",  "
        else:
            rep = "<empty>"
        return rep
    def __len__(self):
        return len(self.cards)
    def __getitem__(self, item):
        return self.cards.__getitem__(item)
    def clear(self):
        """Erases all cards in hand"""
        self.cards = []
    def add(self, card):
        """Adds a card, given card object"""
        self.cards.append(card)
    def remove(self, card):
        """Removes a specific card"""
        self.cards.remove(card)
    def give(self, card, other_hand):
        """Removes a specific card and then adds it to another hand"""
        self.cards.remove(card)
        card.number = len(other_hand.cards) 
        other_hand.add(card)
    def steal(self, card, other_hand):
        """Removes a specific card from another hand and then adds it"""
        other_hand.remove(card)
        self.cards.add(card)
    
    def bubble_sort(self, trump = None):
        """Sorts a list in place and returns it. Either by trump if given or by suit.
        Separate the two functions?"""
        cards = self.cards
        for passesLeft in range(len(cards)-1, 0, -1):
            for index in range(passesLeft):
                if (trump == None):
                    if (cards[index] < cards[index + 1]):
                       cards[index], cards[index + 1] = cards[index + 1], cards[index]
                else:
                    if (cards[index].value(trump) < cards[index + 1].value(trump)):
                       cards[index], cards[index + 1] = cards[index + 1], cards[index]
        return cards
    def search(self, suit = None, rank = None):
        """Searches for a type of card and then returns the list of all matches
        Must be better way to accomplish this"""
        cards = self.cards[:]
        for card in cards[:]:
            if ((card.suit != suit and suit != None) or (card.rank != rank and rank != None)):
                cards.remove(card)
        return cards
class trick(hand):
    """Trick is inherited from Hand. Has best_card"""
    def _suits(self, suit):
        lst = []
        for card in self.cards:
            if (card.suit == suit):
                lst.append(card)
        return lst
    def _higher(self, rank):
        lst = []
        for card in self.cards:
            if (card.rank >= rank):
                lst.append(card)
        return lst
    def _lower(self, rank):
        lst = []
        for card in self.cards:
            if (card.rank <= rank):
                lst.append(card)
        return lst
    def _trump(self, trump):
        lst = []
        for card in self.cards:
            if (card.is_trump(trump)):
                lst.append(card)
        return lst
    def _notTrump(self, trump):
        lst = []
        for card in self.cards:
            if (not card.is_trump(trump)):
                lst.append(card)
        return lst
    def _shift(self, n):
        n = n % len(self.cards)
        tail = self.cards[n:]
        self.cards[n:] = []
        tail.extend(self.cards)
        self.cards = tail
                                        
    def best_card(self, trump, allowtrump = 0):
        """Returns the index of the most valuable card"""
        lead = self.cards[0].suit
        best_card = self.cards[0]
        best_value = best_card.value(trump, lead)
        for each_card in self.cards:
            if(each_card.value(trump, lead) > best_value):
                best_card = each_card
                best_value = best_card.value(trump, lead)                
        this = self.cards.index(best_card)
        # This print statement is for debugging
        #print best_card, "is #", this + 1
        return self.cards.index(best_card)

class deck(hand):
    """Deck is inherited from Hand. has: populate, deal, and shuffle"""
    def populate(self):
        """Builds the deck with cards"""
        for suit in suits[1:]:
            for rank in ranks[1:]:
                self.add(card(rank, suit))

    def shuffle(self):
        """Random shuffle function"""
        random.shuffle(self.cards)
    def deal(self, hands, dealer = 0):
        """Basic euchre dealing function"""
        for index in range(1, 5):
            try:
                top_card = self.cards[0]
                self.give(top_card, hands[((dealer + index) % 4)])
                top_card = self.cards[0]
                self.give(top_card, hands[((dealer + index) % 4)])
            except:
                print "Can't continue deal. Out of cards!"
        for index in range(1, 5):
            try:
                top_card = self.cards[0]
                self.give(top_card, hands[((dealer + index) % 4)])
                top_card = self.cards[0]
                self.give(top_card, hands[((dealer + index) % 4)])
                top_card = self.cards[0]
                self.give(top_card, hands[((dealer + index) % 4)])
            except:
                print "Can't continue deal. Out of cards!"
        
class player(trick):
    """Player is inherited from trick, is interactive. Has set_hand, get_play, get_bid, pick_it_up, worst_card and highest_nontrump"""
    def __init__(self, table = None):
        """Blank hand. No Cards yet."""
        self.index = 0
        self.cards = []
        self.name = ""
        self.table = table

    def set_table(self, table):
        self.table = table

    def ask(self, msg = "", played_cards = [], trump = None, top_card = None, dealer = None, error = ""):
        return self.table.display(top_card = top_card, trump = trump, dealer = dealer, played_cards = played_cards, cards = self.cards, msg = msg, error = error)
        
    def set_hand(self, hand):
        """Set_hand assigns the cards to the hand"""
        self.cards = hand.cards
    def good_play(self, card):
        """Checks the validity of a card choice"""
        """Remove this and append to the code where it is,  no reason to have this pulled out"""
        try:
            good_play = (0 < int(card) and int(card) <= len(self.cards))
        except ValueError:
            good_play = ("1" <= card and card <= ["1", "2", "3", "4", "5"][len(self.cards) - 1])
        return good_play        
    
    def get_play(self, trump, played_cards):
        """Finds the card to play by prompting the user for input."""
#        for i in range(len(self.cards)):
#            print "        ",  i + 1,
        card = self.ask(msg = "Which card would you like to play? ", played_cards = played_cards, trump = trump)
        card = ((card + " ").upper()[0])
        while(not self.good_play(card)):
            if (card == "q" or card == "Q"):    exit()            
            card = self.ask(msg = "Which card would you like to play? ", error = "invalid card", played_cards = played_cards, trump = trump)
            card = ((card + " ").upper()[0])
        #print "You picked:", card, " of ", self
        #print "played cards ", played_cards
        return self.cards[int(card) - 1]
    def bid(self, top_card = 0, dealer = 0):
        """Retrieves the bid from a player"""
        if(top_card == 0):
            bid = self.ask(msg = "Your bid: Spades, Clubs, Diamonds, Hearts or Pass? ")
            bid = bid.upper()
            #bid = ((bid + " ").upper()[0])
            while(1):
                if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
                    return bid
                elif (bid == "Q"):
                    exit()
                elif (bid == "P"):
                    break
                else:
                    bid = self.ask(msg = "Your bid: Spades, Clubs, Diamonds, Hearts or Pass? ", error = "invalid bid")
                    bid = bid.upper()
        else:
            if (dealer == self.index): msg = "\t Pick it up? "
            else: msg = "\tOrder it up? " 
            bid = self.ask(msg = msg, dealer = dealer, top_card = top_card)
            bid = bid.upper()
            while(1):
                if (bid == "Y"):
                    return top_card.suit
                elif (bid == "N" or bid == "P"):
                    break
                elif (bid == "Q"):
                    exit()
                else:
                    bid = self.ask(msg = msg, error="Invalid Bid", dealer = dealer, top_card = top_card)
                    bid = bid.upper()
        return bid
    def pick_it_up(self, top_card):
        """Function that handles adding a card to the deck and then discarding a card."""
        self.add(top_card)
        card = self.ask(msg = "Which card do you want to discard? ")
        card = card.upper()
        while(not ("1" <= card and card <= "6")):
            if (card == "Q"):
                exit()            
            card = self.ask(msg = "Which card do you want to discard? ", error="Invalid Card")
            card = card.upper()
        index = 0        
        for i in ["1", "2", "3", "4", "5", "6"]:
            if (i == card):
                self.remove(self.cards[index])
            index += 1
        #print "\033[2J\033[0;0H",
    def worst_card(self, trump):
        """Returns the lowest valued card
        Replace with sort()[:1] ?"""
        lead = self.cards[0].suit
        best_card = self.cards[0]
        best_value = best_card.value(trump, lead)
        for each_card in self.cards:
            if(each_card.value(trump, lead) > best_value):
                best_card = each_card
                best_value = best_card.value(trump, lead)                
        this = self.cards.index(best_card)
        # This print statement is for debugging
        #print best_card, "is #", this + 1
        return self.cards.index(best_card)
    def best_card(self, trump):
        """Returns the highest valued card
        Use trick? Replace with sort()[1:] ?"""
        lead = self.cards[0].suit
        best_card = self.cards[0]
        best_value = best_card.value(trump, lead)
        for each_card in self.cards:
            if(each_card.value(trump, lead) > best_value):
                best_card = each_card
                best_value = best_card.value(trump, lead)                
        this = self.cards.index(best_card)
        # This print statement is for debugging
        #print best_card, "is #", this + 1
        return self.cards.index(best_card)
    def tip():
        """Suggest a move to the player using comp() to analyze the situation"""
        pass


class comp(player):
    """Player is inherited from hand, is a "computer" player and has limited AI. Has get_play, get_bid, pick_it_up"""
    """ Cards that it can beat vs cards that beat it"""
    
    def get_play(self, trump, played_cards):
        """Return the play from the "player" Compare the AI to the Human."""
        return self.get_play_test(trump, played_cards)
    def get_play_test(self, trump, played_cards):
        """Return the play from the "player" Compare the AI to the Human."""
        #p1 = player.get_play(self, trump, played_cards)
        p2 = self.get_play_ai(trump, played_cards)
        #p2 = self.get_play_ai_try(trump, played_cards)
        #if p1 != p2:
        #    print "error!"
        #else:
        #    print "pass"
        return p2
    def get_play_ai(self, trump, played_cards):
        def first():
            """leader plays highest card or highest non-trump"""
            #self.cards.bubble_sort(trump)
            #if (self.card[0].value(trump) == values["JT"]):
            #    return self.card[0]
            #else:
            try:
                cards = hand()
                cards.steal(self, card("J", trump))
                card = cards.pop(0)
                self.add(card)
            except:
                cards = self._notTrump(trump)
                if len(cards):
                    card = cards.pop(0)
            finally:
                if 'card' not in locals():    
                    card = self.cards[0]
            return card
        def second():
            """follow suit highest
            lowest else lowest trump
            lowest card"""
            #self.cards.bubble_sort(trump)
            lead = played_cards[0]
            cards = trick()
            if (lead.is_trump(trump)):
                cards.cards = self._trump(trump)
                high = cards._higher(lead.rank)
                lower = cards._lower(lead.rank)
                if (len(high)):
                    card = high.pop(0)
                if ((len(lower)) and ('card' not in locals())):
                    card = lower.pop(-1)
                #print "a", locals()
                if 'card' not in locals():
                    card = self._notTrump(trump)[-1]    
            else:
                cards.cards = self._notTrump(trump)
                cards.cards = cards._suits(lead.suit)
                high = cards._higher(lead.rank)
                lower = cards._lower(lead.rank)
                trump_lst = self._trump(trump)
                if (len(high)):
                    #print high
                    card = high.pop(0)
                if ((len(lower)) and ('card' not in locals())):
                    #print lower
                    card = lower.pop(-1)
                if ((len(trump_lst)) and ('card' not in locals())):
                    #print trump_lst
                    card = self._trump(trump)[-1]
                #print "b", locals()
                if 'card' not in locals():
                    card = self._notTrump(trump)[-1]
            return card                
        def third():
            """if two winning hand play like two
            else throw smallest card"""
            #self.cards.bubble_sort(trump)
            if(played_cards[0].value(trump) < played_cards[1].value(trump)):
                #print "Play like two"
                card = second()
            else:
                lead = played_cards[0]
                cards = trick()
                if (lead.is_trump(trump)):
                    #print "this 1"
                    cards.cards = self._trump(trump)
                    lower = cards._lower(lead.rank)
                    high = cards._higher(lead.rank)
                    if (len(lower)):
                        card = lower.pop(-1)
                    if ((len(high)) and ('card' not in locals())):
                        card = high.pop(-1)
                    if not 'card' in locals():
                        card = self._notTrump(trump)[-1]    
                else:
                    #print "this 2"
                    cards.cards = self._notTrump(trump)
                    cards.cards = cards._suits(lead.suit)
                    lower = cards._lower(lead.rank)
                    try:
                        card = lower.pop(-1)
                    except:
                        card = self.cards[-1]
            return card
        def last():
            """if two is winning play lowest
            else lowest to take trick"""
            #self.cards.bubble_sort(trump)
            lead = played_cards[0]
            cards = trick()
            if (played_cards[0].value(trump) < played_cards[1].value(trump) and played_cards[2].value(trump) < played_cards[1].value(trump)):
                #print "this 1"
                if (lead.is_trump(trump)):
                    #print "this 2"
                    cards.cards = self._trump(trump)
                    lower = cards._lower(lead.rank)
                    high = cards._higher(lead.rank)
                    if (len(lower)):
                        card = lower.pop(-1)
                    if ((len(high)) and ('card' not in locals())):
                        card = high.pop(-1)
                    if not 'card' in locals():
                        card = self._notTrump(trump)[-1]    
                else:
                    #print "this 3"
                    cards.cards = self._notTrump(trump)
                    cards.cards = cards._suits(lead.suit)
                    lower = cards._lower(lead.rank)
                    try:
                        card = lower.pop(-1)
                    except:
                        card = self.cards[-1]
            else:
                if (lead.is_trump(trump)):
                    #print "this 4"
                    cards.cards = self._trump(trump)
                    high = cards._higher(lead.rank)
                    lower = cards._lower(lead.rank)
                    if (len(high)):
                        card = high.pop(-1)
                    if (len(lower)):
                        card = lower.pop(-1)
                    if 'card' not in locals():
                        card = self._notTrump(trump)[-1]    
                else:
                    #print "this 5"
                    cards.cards = self._notTrump(trump)
                    cards.cards = cards._suits(lead.suit)
                    high = cards._higher(lead.rank)
                    lower = cards._lower(lead.rank)
                    trump_lst = self._trump(trump)
                    if(len(high)):
                        #print "this 6"
                        card = high.pop(-1)
                    if ((len(trump_lst)) and ('card' not in locals())):
                        #print "that 1"
                        card = self._trump(trump)[-1]
                    if 'card' not in locals():
                        #print "this 3"
                        card = self._notTrump(trump)[-1]
            return card
            
        """The new play() function"""
        """Insert thought process here:"""
        num = len(played_cards)
        if(num == 0):
            card = first()
        elif(num == 1):
            card = second()
        elif(num == 2):
            card = third()
        elif(num == 3):
            card = last()
        else:
            print "played cards, raise error", played_cards
            raise IndexError
        return card
    def get_play_ai_try(self, trump, played_cards):
        """AI version of play using try...except"""
        results = hand()
        try:
            print """Try to follow suit"""
            results.cards = self.search(suit = played_cards.cards[0].suit)
            print results
            if ((((ranks.index(trump) + ranks.index(played_cards.cards[0].suit)) % 2) == 0) and (trump != played_cards.cards[0].suit)):
                for card in results.cards:
                    if(card.rank == "J"):
                        results.remove(card(played_cards.cards[0].suit, "J"))
            results.bubble_sort()
            if (len(results.cards) != 1):
                index = random.randrange(0, len(results.cards) - 1)
                index = self.cards.index(results.cards[index])                    
            else:
                index = 0
        except IndexError:
            print """This is the first player of trick aka the Leader"""        
            try:
                print """What should I lead?"""
                if (self.cards[0].value(trump) == 28):
                    index = 0
                else:
                    print """Don't have the right"""
                    for card in self.cards:
                        if (card.value(trump) < 20):
                            print """Highest non-trump"""
                            index = self.cards.index(card)
                            break
                        else:
                            print """All trump???"""
                            index = 0
#                index = random.randrange(0, len(self.cards) - 1)
            except ValueError:
                print """This is the last trick"""
                index = 0
        except ValueError:
            print """Can't follow suit (not leader)"""
            try:
                results.cards = self.search(suit = trump)
                print results
                results.bubble_sort()
                if (len(results.cards > 1)):
                    index = random.randrange(0, len(results.cards) - 1)
                else:
                    index = 0
            except ValueError:
                print """No trump... through smallest card"""
                cards = self.search(rank = self.cards[len(self.cards) - 1].rank)
                try:
                    print """More than one?"""
                    index = random.randrange(0, len(cards) - 1)
                except ValueError:
                    print """The first (and only) one"""
                    index = 0
                finally:
                    print """Reassign index from "cards" to self.cards"""
                    index = self.cards.index(cards[index])                    
            except:
                print """This is the last trick"""
                index = 0
        else:
            pass
        finally:
            pass
        print "(" , self.index, ": " , self.cards[index] , ")", self
        
        return self.cards[index]
        
    def get_play_with_ifs():
        """AI play rewritten without try...except"""
        index = 0
        this = player()
        this.set_hand(played_cards)
        if (len(played_cards.cards) > 0):
            if (len(self.search(played_cards.cards[0].suit)) > 0):
                cards = self.search(played_cards.cards[0].suit)
                for card in cards:
                    print card,
                print
                this.bubble_sort(trump)
                index = len(cards) - 1
                for card in cards:
                    if (card.value(trump) > played_cards.cards[0].value(trump)):
                        index = cards.index(card)
            elif(len(self.search(trump)) > 0):
                cards = self.search(trump)
                this.bubble_sort(trump)
                index = len(cards) - 1
                for card in cards:
                    if (card.value(trump) > played_cards.cards[0].value(trump)):
                        index = cards.index(card)
            else:
                pass
#                index = random.randrange(0, len(self.cards) - 1)
        else:
            cards = self.cards
            if ((cards[0].value(trump)) > 27):
                index = 0
            else:
                for card in cards:
                    if card.value(trump) < 20:
                        index = cards.index(card)
                        break
         
        # This print is for debugging        
        print "(" , self.index, ": " , self.cards[index] , ")", self
        return self.cards[index]

    def bid(self, top_card = 0, dealer = 0):
        """Get the ai bid"""
        bid = "P"
        if top_card == 0:
            """Everyone Passed"""
            for suit in suits: 
                if self.value(suit) > 85:
                    bid = suit
        elif dealer != 0:
            """Put Intelligent bidding ie do and don't order put etc..."""
            if (self.value(top_card.suit) > 85):
                bid = top_card.suit        
        else:
            """Top Card exists, check score (stupid bidding) """
            if (self.value(top_card.suit) > 85):
                bid = top_card.suit

#        bid = suits[random.randrange(0,5)]
#        if (bid == None or top_card != 0): bid = "P"

        return bid

    def value(self, trump):
        """Returns the lump sum of the values of every card"""
        value = 0
        for card in self.cards:
            value += card.value(trump)
        return value    
    def pick_it_up(self, top_card):
        """Handle adding card to hand and removing the worst"""
        self.add(top_card)
        index = 0
        #index = random.randrange(0, len(self.cards) - 1)
        self.bubble_sort(top_card.suit)
        self.remove(self.cards[-1])
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
#        self.players = [player(), player(), player(), player(), ] 
#        self.players = [player(), comp(), player(), comp(), ] 
#        self.players = [comp(), comp(), comp(), comp(), ] 
        for each_player in self.players:
            each_player.set_table(self)
        self.players[0].name = "Paul"
        self.players[1].name = "Phil"
        self.players[2].name = "Sierra"
        self.players[3].name = "Julia"
    def __str__():
        pass
    def display(self, top_card = None, trump = None, dealer = 0, played_cards = [], cards = [], msg = "", error = ""):
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
            if dealer == 0:
                stdscr.addstr("*1*: ")
            else:    
                stdscr.addstr("1: ")
            printCard(p1)
            #partner
            #stdscr.move(1, 22)
            #stdscr.addstr("[]")
            stdscr.move(2, 22)
            if dealer == 1:
                stdscr.addstr("*P*: ")
            else:    
                stdscr.addstr("P: ")
            printCard(pa)
        
            #player3
            stdscr.move(12, 44)
            if dealer == 2:
                stdscr.addstr("*3*: ")
            else:    
                stdscr.addstr("3: ")

            printCard(p3)
            
            #you
            stdscr.move(22, 22)
            if dealer == 3:
                stdscr.addstr("*U*: ")
            else:    
                stdscr.addstr("U: ")
            printCard(u)
            
            #points
            stdscr.move(21,44)
            stdscr.addstr("Team 1: " + str(self.game.team[0]))
            stdscr.move(22,44)
            stdscr.addstr("Team 2: " + str(self.game.team[1]))
        
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

                for card in cards:
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
        players = table.players
        bid = ""
        self.dealer = random.randrange(0,4)
#        self.dealer = 0
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
        del self.dealer
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
            _trick._shift(1 - leader)
#            #print "\033[2J\033[0;0H",
            #This is a print statement used for debugging
             #print "(",leader,"+",winner,") % 4 =", leader+winner, "% 4 =", (leader+winner) % 4
            msg = ("The winner was: " + str(winner) + " = " + str(_trick.cards[winner]))
            self.table.display(msg = msg, played_cards = _trick)
            leader = winner
            if (leader % 2):
                team += 1
            else:
                team -= 1
            
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
                return (bid, ((self.dealer + index) % 4))
        for index in range(1, 5):
            bid = players[((self.dealer + index) % 4)].bid()
            if self.good_bid(bid):
                return (bid, ((self.dealer + index) % 4))
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
        self.team = [0, 0]
        self.table = table()
        
        index = 0
        self.game = game()
        while(self.team[0] < 10 and self.team[1] < 10):
            self.table.start(self)
            self.game.start(self.table)
            (mybid, index) = self.game.bid(self.table.players)
            if (mybid == "P"):
                continue
            print "mybid, index", mybid, index
            result = self.game.play(self.table.players, mybid)            
            #result = self.bid.play(self.table.players)
            if (result == 5):
                self.team[index % 2] += 2
                print "Team %c gains 2" % (['A', 'B'][index % 2])
            elif (result > 0):
                self.team[index % 2] +=1
                print "Team %c gains 1" % (['A', 'B'][index % 2])
            elif (result < 0):
                self.team[(index + 1) % 2] +=2
                print "Team %c euchred. Team %c gains 2" % ((['A', 'B'][(index) % 2]),(['A', 'B'][(index + 1) % 2]))
            else:
                raise IndexError
        if (self.team[0] > 10):
            print "Team A wins!... 0, 2"
        else:
            print "Team A wins!... 1, 3"

                
                 

def main():
    euchre()

if __name__ == "__main__":
    main()

