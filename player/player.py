from basics import trick#, suits

#suits = [None, "S", "D", "C", "H"]


class player(trick):
    """A simple shell player is inherited from trick, is interactive. No "graphics" """
    def msg(self, msg, quit):
        answer = self.ask(msg = msg, quit = quit)
        if answer == "Q":
            print "someone quit"
            quit()#exit()
            pass

    def results(self, winner, leader, played_cards, team, players, dealer):
        perspective = trick()
        try:
            #msg = ("The winner was: " + str(winner.owner + leader) + " = " + str(played_cards.cards[(leader + winner.owner) % 4]))
            msg = ("The winner was: " + str(winner) + "\n")
        except:
            #msg = ("The winner was: " + str(winner.owner + leader))
            msg = ("The winner was: " + str(winner) + "\n")
        shift = (self.index - leader + 1)
        perspective.cards = played_cards._shift(shift)
        players = players[self.index:] + players[:self.index]
        dealer = ((dealer - self.index) % 4)
        answer = self.ask(msg = msg, played_cards = perspective, team = team, players = players, cards = self.cards, dealer = dealer)
        if answer == "Q":
            print "someone quit"
            quit()#exit
            pass

        leader = winner
    
    def play(self, trump, played_cards, dealer, team, players):
        """Finds the card to play by prompting the user for input."""
#        for i in range(len(self.cards)):
#            print "        ",  i + 1,
        players = players[self.index:] + players[:self.index]
        dealer = ((dealer - self.index) % 4)

        card = self.ask(msg = "Which card would you like to play? ", played_cards = played_cards, trump = trump, dealer = dealer, team = team, players = players, cards = self.cards)
        card = ((card + " ").upper()[0])
        while(not self.good_play(card)):
            if (card == "Q"):    quit()#exit()            
            if (card == "I"):
                card = self.ask(msg = "Which card would you like to play? ", played_cards = played_cards, trump = trump, players = players, dealer = dealer, team = team, secret = 1, cards = self.cards)
            else:
                card = self.ask(msg = "Which card would you like to play? ", error = "invalid card", played_cards = played_cards, trump = trump, dealer = dealer, team = team, cards = self.cards)
            card = ((card + " ").upper()[0])
        #print "You picked:", card, " of ", self
        #print "played cards ", played_cards
        return self.cards[int(card) - 1]
    def bid(self, top_card = 0, dealer = 0, players = 0, team = [98,98]):
        """Retrieves the bid from a player"""
        dealer = ((dealer - self.index) % 4)

        if(top_card == 0):
            self.bubble_sort()
            bid = self.ask(msg = "Your bid: Spades, Clubs, Diamonds, Hearts or Pass? ", dealer = dealer, team = team, cards = self.cards)
            bid = bid.upper()
            #bid = ((bid + " ").upper()[0])
            while(1):
                if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
                    return bid
                elif (bid == "Q"):
                    quit() #exit()
                elif (bid == "P"):
                    break
                else:
                    bid = self.ask(msg = "Your bid: Spades, Clubs, Diamonds, Hearts or Pass? ", error = "invalid bid", dealer = dealer, team = team, cards = self.cards)
                    bid = bid.upper()
        else:
            self.bubble_sort(top_card.suit)
            if (dealer == self.index): msg = "\t Pick it up? "
            else: msg = "\tOrder it up? " 
            bid = self.ask(msg = msg, top_card = top_card, dealer = dealer, team = team, cards = self.cards)
            bid = bid.upper()
            while(1):
                if (bid == "Y"):
                    return top_card.suit
                elif (bid == "N" or bid == "P"):
                    break
                elif (bid == "Q"):
                    quit() #exit()
                else:
                    bid = self.ask(msg = msg, error="Invalid Bid", top_card = top_card, dealer = dealer, team = team, cards = self.cards)
                    bid = bid.upper()
        return bid
    def pick_it_up(self, top_card, dealer, team):
        """Function that handles adding a card to the deck and then discarding a card."""
        dealer = ((dealer - self.index) % 4)

        self.add(top_card)
        self.bubble_sort(top_card.suit)
        card = self.ask(msg = "Ordered up. Which card do you want to discard? ", dealer = dealer, top_card = top_card, team = team, cards = self.cards)
        card = card.upper()
        while(not ("1" <= card and card <= "6")):
            if (card == "Q"):
                quit() #exit()            
            card = self.ask(msg = "Which card do you want to discard? ", error="Invalid Card", dealer = dealer, top_card = top_card, team = team, cards = self.cards)
            card = card.upper()
        index = 0        
        for i in ["1", "2", "3", "4", "5", "6"]:
            if (i == card):
                self.remove(self.cards[index])
            index += 1

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
    def set_hand(self, hand):
        """Set_hand assigns the cards to the hand"""
        self.cards = hand.cards
    def tip():
        """Suggest a move to the player using comp() to analyze the situation"""
        pass
    
    def good_play(self, card):
        """Checks the validity of a card choice"""
        """Remove this and append to the code where it is,  no reason to have this pulled out"""
        try:
            good_play = (0 < int(card) and int(card) <= len(self.cards))
        except ValueError:
            good_play = ("1" <= card and card <= ["1", "2", "3", "4", "5"][len(self.cards) - 1])
        return good_play        

    def __getstate__(self):
        return self.tricks_taken, trick.__getstate__(self)
    def __setstate__(self, state):
        self.tricks_taken, state = state
        trick.__setstate__(self,state)
    def ask(self, **data):
        """Dummy Player, plays "default values." great for testing"""
        from cPickle import load, dump
        
#        print data['msg']
#        print "09 dealer: ", data['dealer']
#        print "self.index: ", self.index

        with open("data", "w") as f:
            dump(data, f)
        msg = data["msg"]
        
        dealer = data['dealer']
        if 1: # ON/OFF
            pass
        elif dealer == 0:
            print " x \nx x\n D "
        elif dealer == 1:
            print " x \nD x\n x "
        elif dealer == 2:
            print " D \nx x\n x "
        elif dealer == 3:
            print " x \nx D\n x "
        else:
            print "dealer:", dealer
            raise Exception("dealer wrong.")

        if (msg[:7] == "The win"): # Results
            return
        elif (msg[-6:] == "play? "): # Play
#            if len(data['played_cards']) > 1:
#                quit()
            return "1"
        elif (msg[-4:] == "up? "):
#            quit()
            return "Y"
        elif (msg[-6:] == "Pass? "): # Bid
            return "S"
        elif (msg[-9:] == "discard? "): # Pick it Up
            return "6"
        else: # Bad
            print "|%s|" % msg
            raise Exception("msg finder failed")
