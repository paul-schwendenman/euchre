from player import *

class comp(player):
    """Comp is inherited from player, is a "computer" player and has limited AI. Has get_play, get_bid, pick_it_up"""
    """ Cards that it can beat vs cards that beat it"""
    def msg(self, msg, number = 0, list = []):
        pass
    
    def play(self, trump, played_cards, dealer, team, players):
        """Return the play from the "player" Compare the AI to the Human."""
        return self.ai(trump, played_cards)
    def get_play_test(self, trump, played_cards):
        """Return the play from the "player" Compare the AI to the Human."""
        #p1 = player.get_play(self, trump, played_cards)
        p2 = self.ai(trump, played_cards)
        #p2 = self.get_play_ai_try(trump, played_cards)
        #if p1 != p2:
        #    print "error!"
        #else:
        #    print "pass"
        return p2
    def results(self, winner, leader, played_cards, team, players, dealer):
        pass
    def ai(self, trump, played_cards):
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

    def bid(self, top_card = 0, dealer = 0, players = 0, team = [98, 98]):
        """Get the ai bid"""
        bid = "P"
        if top_card == 0:
            """Everyone Passed"""
            values = []
            for suit in enumerate(suits): 
                values.append(self.value(suit))
            values.sort()
            value = values.pop()      
            if value > 85:
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
    def pick_it_up(self, top_card, dealer, team):
        """Handle adding card to hand and removing the worst"""
        self.add(top_card)
        index = 0
        #index = random.randrange(0, len(self.cards) - 1)
        self.bubble_sort(top_card.suit)
        self.remove(self.cards[-1])
        return "6"
    def ask(self, **kwargs):
        msg = kwargs["msg"]
        self.cards = kwargs["cards"]
        if (msg[:7] == "The win"): # Results
            pass
        elif (msg[-6:] == "play? "): # Play
            return self.play(kwargs["trump"], kwargs["played_cards"], kwargs["dealer"], kwargs["team"], kwargs["players"])
        elif (msg[-4:] == "up? " or msg[-6:] == "Pass? "): # Bid
            try:
                return self.bid(kwargs["top_card"], kwargs["dealer"], kwargs["players"], kwargs["team"])
            except KeyError:
                try:
                    return self.bid(kwargs["top_card"], kwargs["dealer"])
                except KeyError:
                    return self.bid()            
        elif (msg[:5] == "Order"): # Pick it Up
            return self.pick_it_up(kwargs["top_card"], kwargs["dealer"], kwargs["team"])
        else: # Bad
            print "|%s|" % msg
            raise Exception("Should have called one of those ^")

