import random

# Constants for the euchre game.
ranks = [None, "9", "10", "J", "Q", "K", "A",]
cardname = [None, "9", "10", "J", "Q", "K", "A", "9T", "10T", "QT", "KT", "AT", "LB", "JT"]
cardvalu = [  -1,  1 ,   2 ,  3 ,  4 ,  5 ,  10,  12 ,   15 ,  20 ,  25 ,  30 ,  31 ,  35 ]
values = dict(zip(cardname, cardvalu))
left = { "S" : "C", "C" : "S", "D" : "H", "H" : "D"}
suits = [None, "S", "D", "C", "H"]
suit_chars = [None, unichr(9824), unichr(9827), unichr(9829), unichr(9830)]
#suit_chars = [None, 9824, 9827, 9829, 9830]
bower = "J"


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
        elif (self.rank == bower and trump == left[self.suit]):
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
    def __getstate__(self):
        return self.rank, self.suit
    def __setstate__(self, state):
        self.rank, self.suit = state        

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
        try:
            card.owner = self.index
        except:
            raise Exception("No owner")
        other_hand.add(card)
    def steal(self, card, other_hand):
        """Removes a specific card from another hand and then adds it"""
        other_hand.remove(card)
        try:
            card_owner = other_hand.index
        except:
            pass
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
    def __getstate__(self):
        if self.cards:
            cards = [card.__getstate__() for card in self.cards]
        else:
            cards = self.cards
        return self.name, self.index, cards
    def __setstate__(self, state):
        self.name, self.index, cards = state
        self.cards = []
        for index, _card_ in enumerate(cards):
            self.cards.append(card(*_card_))
        
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
    def _split(self, n):
        return self.cards[:n], self.cards[n:]

    def _shift(self, n, destructive = 0):
        b, a = self._split(n)
        c = a + b

        if destructive:
            self.cards = c
        else:
            return c
                                        
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
        return best_card

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

