import random

#shuffle
#set scores to zero
##deal cards
##bidding
##lead
##follow suit
##else 
###trump
###throw off



# Constants fo the euchre game.
ranks = [None, "9", "10", "J", "Q", "K", "A",]
cardname = [None, "9", "10", "J", "Q", "K", "A", "9T", "10T", "QT", "KT", "AT", "LB", "JT"]
cardvalu = [  -1,  1 ,   2 ,  3 ,  4 ,  5 ,  10,  12 ,   15 ,  20 ,  25 ,  30 ,  31 ,  35 ]
values = dict(zip(cardname, cardvalu))
left = { "S" : "C", "C" : "S", "D" : "H", "H" : "D"}
suits = [None, "S", "D", "C", "H"]
suit_chars = [None, unichr(9824), unichr(9827), unichr(9829), unichr(9830)]
#suit_chars = [None, 9824, 9827, 9829, 9830]


class card:
    """Card class has: __init__, getRank, getSuit, and __str__"""
    def __init__(self, rank = None, suit = None):
        """Makes a new card. by default the card is blank or has no suit or value (rank)."""
        self.rank = rank
        self.suit = suit
        self.ranks = ranks
        self.suits = suits
    def getRank(self):
        """returns the rank of the card, i.e. 9 or J"""
        """remove?"""
        return self.rank
    def getSuit(self):
        """returns the suit of the card, i.e. S or D"""
        """remove?"""
        return self.suit
    def value(self, trump, lead = None):
        """Calculates the value of the card bassed on trump and a lead?
        better was to do this?"""
        if (self.suit == trump):
            value = values[self.rank + "T"]
        elif (self.rank == "J" and trump == left[self.suit]):
            value = values["LB"]
        else:
            value = values[self.rank]
            

#        try:
#            value = ranks.index(self.rank)
#        except:
#            print self.rank, "is not in", ranks
#            exit()
#        if (self.suit == trump):
#            value += 20
#            if (self.rank == "J"):
#                value = 28
#        elif (((suits.index(self.suit) + suits.index(trump)) % 2 == 0) and self.rank == "J"):
#            value = 27
#        elif (self.suit == lead):
#            value += 10

        #This print statement is for debugging
        #print "rank: %2i card: %s trump %s" % (value, self, trump)

        return value
    def __str__(self):
        """prints information of the card in the form: R of S, where R is rank and S is suit"""
        output = ""
#            output += "%2s of %s" % (self.ranks[self.rank], self.suits[self.suit])
        if (self.suit == "d" or self.suit == "D" or self.suit == "h" or self.suit == "H"):
            output += "\033[0;31m"
        output += "%2s of %s" % (self.rank, self.suit) + "\033[m"
#        output += "%2s of" % (self.rank) + suit_chars[suits.index(self.suit)] + "\033[m"
        return output


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
        other_hand.add(card)
    def steal(self, card, other_hand):
        """Removes a specific card from another hand and then adds it"""
        other_hand.remove(card)
        self.cards.add(card)
    
    def bubble_sort(self, trump = None):
        """Sorts a list in place and returns it. Either by trump if given or by suit."""
        """Separate the two functions?"""
        cards = self.cards
        for passesLeft in range(len(cards)-1, 0, -1):
            for index in range(passesLeft):
                if (trump == None):
                    if (cards[index] < cards[index + 1]):
                       cards[index], cards[index + 1] = cards[index + 1], cards[index]
                else:
                    if (cards[index].value(trump) < cards[index + 1].value(trump)):
                       cards[index], cards[index + 1] = cards[index + 1], cards[index]
        self.cards = cards
    def search(self, suit = None, rank = None):
        """Searches for a type of card and then returns the list of all matches"""
        """Must be better way to accomplish this"""
        cards = self.cards[:]
        for card in cards[:]:
            if ((card.suit != suit and suit != None) or (card.rank != rank and rank != None)):
                cards.remove(card)
        return cards
class trick(hand):
    """Trick is inherited from Hand. Has best_card"""
    def best_card(self, trump):
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
        
class player(hand):
    """Player is inherited from trick, is interactive. Has set_hand, get_play, get_bid, pick_it_up, worst_card and highest_nontrump"""
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
        #print "\033[2J\033[0;0H",
        print "Cards played so far:", played_cards
        print "Your hand", self.index + 0, "\033[1D:" , self,
        print "Trump is: ", trump
        print "     ",
        for i in range(len(self.cards)):
            print "        ",  i + 1,
        print
        card = ((raw_input("Which card would you like to play? ") + " ").upper()[0])
        while(not self.good_play(card)):
            if (card == "q" or card == "Q"):    exit()            
            print "\033[1A\033[35Cinvalid input"
            card = (raw_input("Which card would you like to play? ") + " ").upper()[0]
        index = 0        
        for i in ["1", "2", "3", "4", "5"]:
            if (i == card):
                return self.cards[index]
            index += 1
    def bid(self, top_card = 0, dealer = 0):
        """Retrieves the bid from a player"""
        if(top_card == 0):
            #print "\033[2J\033[0;0H",
            print "\nYour hand", self.index + 0, "\033[1D:", self
            bid = (raw_input("\tYour bid: Spades, Clubs, Diamonds, Hearts or Pass? ") + " ").upper()[0]
            while(1):
                if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
                    return bid
                elif (bid == "Q"):
                    exit()
                elif (bid == "P"):
                    break
                else:
                    print "\033[1A\033[59Cinvalid input"
                    bid = (raw_input("\tYour bid: Spades, Clubs, Diamonds, Hearts or Pass? ") + " ").upper()[0]
        else:
            #print "\033[2J\033[0;0H",
            if (dealer == self.index): msg = "\t Pick it up? "
            else: msg = "\tOrder it up? " 
            print "\nYour hand", self.index + 0, "\033[1D:" , self
            print "the top card is", top_card
            print "the dealer is", dealer + 0
            bid = (raw_input(msg) + " ").upper()[0]
            while(1):
                if (bid == "Y"):
                    return top_card.suit
                elif (bid == "N" or bid == "P"):
                    break
                elif (bid == "Q"):
                    exit()
                else:
                    print "\033[1A\033[21Cinvalid input"
                    bid = (raw_input(msg) + " ").upper()[0]
        return bid
    def pick_it_up(self, top_card):
        """Function that handles adding a card to the deck and then discarding a card."""
        self.add(top_card)
        #print "\033[2J\033[0;0H",
        print "Your hand", self.index + 0, "\033[1D:" , self
        print "     ",
        for i in range(len(self.cards)):
            print "        ",  i + 1,
        print
        card = (raw_input("Which card do you want to discard? ") + " ").upper()[0]
        while(not ("1" <= card and card <= "6")):
            if (card == "Q"):
                exit()            
            print "\033[1A\033[35Cinvalid input"
            card = (raw_input("Which card do you want to discard? ") + " ").upper()[0]
        index = 0        
        for i in ["1", "2", "3", "4", "5", "6"]:
            if (i == card):
                self.remove(self.cards[index])
            index += 1
    def worst_card(self, trump):
        """Returns the lowest valued card"""
        """Replace with sort()[:1] ?"""
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
        """Returns the highest valued card"""
        """Use trick? Replace with sort()[1:] ?"""
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
    
#    def get_play(self, trump, played_cards):
        #return self.get_play_ai(trump, played_cards)
    def get_play_ai(self, trump, played_cards):
        """AI version of play, brains here?"""
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
                bid = suit        
        else:
            """Top Card exists, check score (stupid bidding) """
            if (self.value(top_card.suit) > 85):
                bid = suit

#        bid = suits[random.randrange(0,5)]
#        if (bid == None or top_card != 0): bid = "P"

        return bid

    def value(self):
        """Returns the lump sum of the values of every card"""
        for card in self.cards:
            value += card.value
        return value    
    def pick_it_up(self, top_card):
        """Handle adding card to hand and removing the worst"""
        self.add(top_card)
        index = 0
        index = random.randrange(0, len(self.cards) - 1)
        self.remove(self.cards[index])
class table:
    """Class for the table, has players."""
    def __init__(self):
        pass

    def start(self):
        """begins a game by adding players"""
        num_players = 0
        self.players = []
#            self.players = [player(), comp(), comp(), comp(), ] 
#            self.players = [player(), player(), player(), player(), ] 
#            self.players = [player(), comp(), player(), comp(), ] 
        self.players = [comp(), comp(), comp(), comp(), ] 
        self.players[0].name = "Paul"
        self.players[1].name = "Phil"
        self.players[2].name = "Sierra"
        self.players[3].name = "Julia"

    
class bid:
    """Class for each hand in a game, meaning all the stuff needed to play for one hand."""
    def __init__(self):
        pass


    def start(self, players):
        """Starts up the deck and deals"""
        bid = ""
        self.dealer = random.randrange(0,4)
#        self.dealer = 0
        self.deck = deck()
        self.deck.populate()
        self.deck.bubble_sort()
        self.deck.shuffle()
        self.deck.deal(players, self.dealer)

        for each_player in players:
            each_player.index = players.index(each_player)
            each_player.bubble_sort()


    def bid():
        """Handles bidding for all players"""
        top_card = self.deck.cards[0]
        bid = self.bid(players, top_card)
        return bid
    def play(self, players, bid = 'S'):
        """Handles the card play given a bid"""
        trump = bid
        played_cards = hand()
        del bid
        print "trump:\t\t", trump, "\ndealer:\t\t", self.dealer
        for each_player in players:
            each_player.bubble_sort(trump)
        leader = self.dealer + 1
        del self.dealer
        tricks = 5 * [trick()] #tricks = [trick(), trick(), trick(), trick(), trick(),]
        for each_trick in tricks:
            each_trick = self.get_play(players, trump, leader)
            winner = each_trick.best_card(trump)
#            #print "\033[2J\033[0;0H",
            #This is a print statement used for debugging
             #print "(",leader,"+",winner,") % 4 =", leader+winner, "% 4 =", (leader+winner) % 4
            print "The winner was: ", (leader + winner) % 4, " = ", each_trick.cards[winner], "of", each_trick
            leader = leader + winner
        for each_trick in tricks:
            while (len(each_trick.cards) > 0):      
                each_trick.give(played_cards.cards[0], self.deck)
    def get_play(self, players, trump, leader):
        """Handles the card play for all players"""
        played_cards = trick()
        for index in range(0, 4):
            play_this_card2 = players[((leader + index) % 4)].get_play(trump, played_cards)
            play_this_card = players[((leader + index) % 4)].get_play_ai(trump, played_cards)
            if (play_this_card != play_this_card2):
                print "\033[32m\n\033[mERRROR!!!!!!!!!!!!!\n"
            players[((leader + index) % 4)].give(play_this_card, played_cards)
        print
        return played_cards

    def get_bid(self, players, top_card):
        """Handles the bid recovery for all players"""
        for index in range(1, 5):
            bid = players[((self.dealer + index) % 4)].get_bid(top_card, self.dealer)
            if self.good_bid(bid):
                players[self.dealer].pick_it_up(top_card)
                return bid
        for index in range(1, 5):
            bid = players[((self.dealer + index) % 4)].get_bid()
            if self.good_bid(bid):
                return bid
        return bid

#    def good_bid(self, bid):
#        """tests to see if the bid is "Good" """
#        if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
#            return 1
#        else:
#            return 0



class euchre:
    """Highest level class creates a game for play"""
    def __init__(self):
        """Sets up and starts a game."""
        self.table = table()
        self.table.start()
        
        self.bid = bid()
        mybid = self.bid.start(self.table.players)
        self.bid.play(self.table.players, mybid)
    def rank_cards():
        pass        

def main():
    euchre()

if __name__ == "__main__":
    main()

