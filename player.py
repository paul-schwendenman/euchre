from basics import trick, suits

#suits = [None, "S", "D", "C", "H"]


class player(trick):
    """A simple shell player is inherited from trick, is interactive. No "graphics" """
    def set_table(self, table):
        self.table = table

    def results(self, winner, leader, played_cards, team, players):
        perspective = trick()
        try:
            #msg = ("The winner was: " + str(winner.owner + leader) + " = " + str(played_cards.cards[(leader + winner.owner) % 4]))
            msg = ("The winner was: " + str(winner) + "\n")
        except:
            #msg = ("The winner was: " + str(winner.owner + leader))
            msg = ("The winner was: " + str(winner) + "\n")
            print played_cards
        perspective.cards = played_cards._shift(self.index - leader + 1)
        self.display(msg = msg, played_cards = perspective, team = team, players = players)
        print msg
        print "trick: ", played_cards
        print "shift: ", perspective
        leader = winner
    
    def play(self, trump, played_cards, dealer, team, players):
        """Finds the card to play by prompting the user for input."""
#        for i in range(len(self.cards)):
#            print "        ",  i + 1,
        card = self.display(msg = "Which card would you like to play? ", played_cards = played_cards, trump = trump, dealer = dealer, team = team, players = players)
        card = ((card + " ").upper()[0])
        while(not self.good_play(card)):
            if (card == "Q"):    exit()            
            if (card == "I"):
                card = self.display(msg = "Which card would you like to play? ", played_cards = played_cards, trump = trump, players = players, dealer = dealer, team = team, secret = 1)
            else:
                card = self.display(msg = "Which card would you like to play? ", error = "invalid card", played_cards = played_cards, trump = trump, dealer = dealer, team = team)
            card = ((card + " ").upper()[0])
        #print "You picked:", card, " of ", self
        #print "played cards ", played_cards
        return self.cards[int(card) - 1]
    def bid(self, top_card = 0, dealer = 0, players = 0, team = [98,98]):
        """Retrieves the bid from a player"""
        if(top_card == 0):
            self.bubble_sort()
            bid = self.display(msg = "Your bid: Spades, Clubs, Diamonds, Hearts or Pass? ", dealer = dealer, team = team)
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
                    bid = self.display(msg = "Your bid: Spades, Clubs, Diamonds, Hearts or Pass? ", error = "invalid bid", dealer = dealer, team = team)
                    bid = bid.upper()
        else:
            self.bubble_sort(top_card.suit)
            if (dealer == self.index): msg = "\t Pick it up? "
            else: msg = "\tOrder it up? " 
            bid = self.display(msg = msg, top_card = top_card, dealer = dealer, team = team)
            bid = bid.upper()
            while(1):
                if (bid == "Y"):
                    return top_card.suit
                elif (bid == "N" or bid == "P"):
                    break
                elif (bid == "Q"):
                    exit()
                else:
                    bid = self.display(msg = msg, error="Invalid Bid", top_card = top_card, dealer = dealer, team = team)
                    bid = bid.upper()
        return bid
    def pick_it_up(self, top_card, dealer, team):
        """Function that handles adding a card to the deck and then discarding a card."""
        self.add(top_card)
        self.bubble_sort(top_card.suit)
        card = self.display(msg = "Ordered up. Which card do you want to discard? ", dealer = dealer, top_card = top_card, team = team)
        card = card.upper()
        while(not ("1" <= card and card <= "6")):
            if (card == "Q"):
                exit()            
            card = self.display(msg = "Which card do you want to discard? ", error="Invalid Card", dealer = dealer, top_card = top_card, team = team)
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

