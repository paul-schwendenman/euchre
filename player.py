class testPlayer(player):
    """A simple test player is inherited from player, is interactive. No "graphics" """
    def get_play(self, trump, played_cards):
        """Finds the card to play by prompting the user for input."""
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
        print "\033[2J\033d[0;0H",

