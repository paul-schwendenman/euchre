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
    def results(self, winner, leader, played_cards):
        pass
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

