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

ranks = [None, "9", "10", "J", "Q", "K", "A",]
suits = [None, "S", "D", "C", "H"]
#         1    2    3    4
suit_chars = [unichr(9824), unichr(9827), unichr(9829), unichr(9830)]

# card Class
class card:
    """Card class has: __init__, getRank, getSuit, and __str__"""
    def __init__(self, rank = None, suit = None):
        self.rank = rank
        self.suit = suit
        self.ranks = ranks
        self.suits = suits
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def value(self, trump, lead = ""):
        try:
            value = ranks.index(self.rank)
        except:
            print self.rank, "is not in", ranks
            exit()
        if (self.suit == trump):
            value += 20
            if (self.rank == "J"):
                value = 28
        elif (((suits.index(self.suit) + suits.index(trump)) % 2 == 0) and self.rank == "J"):
            value = 27
        elif (self.suit == lead):
            value += 10

        #This print statement is for debugging
        #print "rank: %2i card: %s trump %s" % (value, self, trump)

        return value
    def __str__(self):
        output = ""
#            output += "%2s of %s" % (self.ranks[self.rank], self.suits[self.suit])
        if (self.suit == "d" or self.suit == "D" or self.suit == "h" or self.suit == "H"):
            output += "\033[0;31m"
        output += "%2s of %s" % (self.rank, self.suit) + "\033[m"
        return output

class hand(object):
    """Hand of playing cards, base class __init__, __str__, clear, add, remove, and give"""
    def __init__(self):
        self.index = 0
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + ",  "
        else:
            rep = "<empty>"
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def remove(self, card):
        self.cards.remove(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class trick(hand):
    """Trick is inherited from Hand. Has best_card"""
    def best_card(self, trump):
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
#        for suit in range(len(suits)):
            for rank in ranks[1:]:
#            for rank in range(len(ranks))[1:]:
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
#        for hand in hands:
        for index in range(1, 5):
            try:
                top_card = self.cards[0]
#                self.give(top_card, hand)
                self.give(top_card, hands[((dealer + index) % 4)])
                top_card = self.cards[0]
                self.give(top_card, hands[((dealer + index) % 4)])
                top_card = self.cards[0]
                self.give(top_card, hands[((dealer + index) % 4)])
            except:
                print "Can't continue deal. Out of cards!"
        
class player(hand):
    """Player is inherited from hand, is interactive. Has set_hand, get_play, get_bid, pick_it_up"""
    def set_hand(self, hand):
        """Set_hand assigns the cards to the hand"""
        self.cards = hand.cards
    def get_play(self, trump, played_cards):
        """Finds the card to play by prompting the user for input."""
#        print "\033[2J\033[0;0H",
        print "Cards played so far:", played_cards
        print "Your hand", self.index + 1, "\033[1D:" , self,
        print "Trump is: ", trump
        print "     ",
        for i in range(len(self.cards)):
            print "        ",  i + 1,
        print
        card = ((raw_input("Which card would you like to play? ") + " ").upper()[0])
        while(not ("1" <= card and card <= ["1", "2", "3", "4", "5"][len(self.cards) - 1])):
            if (card == "q" or card == "Q"):    exit()            
            print "\033[1A\033[35Cinvalid input"
            card = (raw_input("Which card would you like to play? ") + " ").upper()[0]
        index = 0        
        for i in ["1", "2", "3", "4", "5"]:
            if (i == card):
                return self.cards[index]
            index += 1
    def get_bid(self, top_card = 0, dealer = 0):
        if(top_card == 0):
#            print "\033[2J\033[0;0H",
            print "\nYour hand", self.index + 1, "\033[1D:", self
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
#            print "\033[2J\033[0;0H",
            print "\nYour hand", self.index + 1, "\033[1D:" , self
            print "the top card is", top_card
            print "the dealer is", dealer + 1
            bid = (raw_input("\tPick it up? ") + " ").upper()[0]
            while(1):
                if (bid == "Y"):
                    return top_card.suit
                elif (bid == "N" or bid == "P"):
                    break
                elif (bid == "Q"):
                    exit()
                else:
                    print "\033[1A\033[20Cinvalid input"
                    bid = (raw_input("\tPick it up? ") + " ").upper()[0]
        return bid
    def pick_it_up(self, top_card):
        self.add(top_card)
#        print "\033[2J\033[0;0H",
        print "Your hand", self.index + 1, "\033[1D:" , self
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
class comp(player):
    """Player is inherited from hand, is a "computer" player and has limited AI. Has get_play, get_bid, pick_it_up"""
    def get_play(self, trump, played_cards):
        try:
            index = random.randrange(0, len(self.cards) - 1)
        except:
            index = 0
        # This print is for debugging        
        #print "(", self.index + 1, self.cards[index], ")\t",
        return self.cards[index]
    def get_bid(self, top_card = 0, dealer = 0):
        bid = "P"        
        bid = suits[random.randrange(0,5)]
        if (bid == None or top_card != 0): bid = "P"
        return bid
    def pick_it_up(self, top_card):
        self.add(top_card)
        index = 0
        index = random.randrange(0, len(self.cards) - 1)
        self.remove(self.cards[index])
class euchre:
    """Highest level class creates a game for play"""
    def __init__(self):
        """Sets up and starts a game."""
        bid = ""
#        dealer = random.randrange(0,4)
        dealer = 0
        while(not self.good_bid(bid)):
            my_deck = deck()
            my_deck.populate()
            my_deck.shuffle()
            players = [player(), comp(), comp(), comp(), ] 
#            players = [player(), player(), player(), player(), ] 
#            players = [player(), comp(), player(), comp(), ] 
#            players = [comp(), comp(), comp(), comp(), ] 
            my_deck.deal(players, dealer)

            for each_player in players:
                each_player.index = players.index(each_player)

            top_card = my_deck.cards[0]
            bid = self.get_bid(players, top_card, dealer)

        trump = bid
        played_cards = hand()
        del bid
        leader = dealer + 1
        del dealer
        dealer = 0
#        tricks = [trick(), trick(), trick(), trick(), trick(),]
        tricks = 5 * [trick()]
        for each_trick in tricks:
            print
            print
            each_trick = self.get_play(players, trump, (dealer + leader) % 4)
#            leader = self.leader_is(leader)[each_trick.best_card(trump)]
            dealer = leader
            leader =  each_trick.best_card(trump)
#            print "\033[2J\033[0;0H",
            print "The winner was: ", (dealer + leader) % 4 + 1, " = ", each_trick.cards[leader], "of", each_trick
            dealer = leader
        for each_trick in tricks:
            while (len(each_trick.cards) > 0):      
                each_trick.give(played_cards.cards[0], my_deck)
    def rank_cards():
        pass        
    def get_play(self, players, trump, leader):
        """Handles the card play for all players"""
        played_cards = trick()
        for index in range(0, 4):
            play_this_card = players[((leader + index) % 4)].get_play(trump, played_cards)
            players[((leader + index) % 4)].give(play_this_card, played_cards)
        print
        return played_cards

    def get_bid(self, players, top_card, dealer):
        """Handles the bid recovery for all players"""
        for index in range(1, 5):
            bid = players[((dealer + index) % 4)].get_bid(top_card, dealer)
            if self.good_bid(bid):
                players[dealer].pick_it_up(top_card)
                return bid
        for index in range(1, 5):
            bid = players[((dealer + index) % 4)].get_bid()
            if self.good_bid(bid):
                return bid
        return bid

    def good_bid(self, bid):
        """tests to see if the bid is "Good" """
        if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
            return 1
        else:
            return 0
    def dealer_is(self, n):
        x = []
        if (n == 0 or n == 4):
            x = [1, 2, 3, 4]
        elif (n == 1 or n == 5):
            x = [2, 3, 4, 1]
        elif (n == 2):
            x = [3, 4, 1, 2]
        elif (n == 3):
            x = [4, 1, 2, 3]
        return x
    def leader_is(self, n):
        return self.dealer_is(n - 1)
    def good_play(self):
        pass
def main():
    euchre()
    
if __name__ == "__main__":
    main()

